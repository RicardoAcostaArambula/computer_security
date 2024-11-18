import socket
import threading

CORRECT_IP = '192.168.178.130' 
CORRECT_PORT = 59999

def handle_user(conn, address):
    print(f"Connection from {address}")

    encrypted_message = "baaab aabbb abbab babaa ababb aabaa baaba aabbb aabaa abbba aaaaa baaab baaab babaa abbab baaaa aaabb"
    conn.sendall(f"The following message has to be decoded to proceed: {encrypted_message}.encode('utf-8')")
    conn.sendall("Hint: Try decoding with Bacon cipher.\n".encode('utf-8'))
    conn.sendall("Use the decoded message in the following command: 'echo <decoded_message> | nc <IP> <port>'".encode('utf-8'))
    conn.sendall("Waiting.....\n".encode('utf-8'))

    decoded_message = "SHOWMETHEPASSWORD"

    while True:
        try:
            #Get user's response
            response = conn.recv(1024).decode('utf-8').strip()
            if response == f"echo {decoded_message} | nc {CORRECT_IP} {CORRECT_PORT}":
                conn.sendall(f"You did it! Here is your next key: '8uff3r_0v3rfl0w'".encode('utf-8'))
                break
            else:
                conn.sendall("Incorrect, keep trying.....".encode('utf-8'))
        except Exception as e:
            print(f"Error handling user {address}: {e}")
            break

    #Close connection
    conn.sendall(b"You solved the challenge! You will be disconnected now.\n")
    conn.close()

def start_server():
    #Start the server & accept connections
    print(f"Welcome to Challenge 4! In this challenge you will connect to netcat using the IP address and port number obtained from the previous challenges.\n")
    print(f"To continue use the following command: 'nc <IP> <port>'")
    
    while True:
        #Waiting for user input to connect
        user_connect = input().strip()
        #Validate user's input
        if user_connect == f"nc {CORRECT_IP} {CORRECT_PORT}":
            print("Starting the server...")
            break
        else:
            print("Incorrect command :( . Please try again.")
    
    #set up server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:  
        server.bind((CORRECT_IP, CORRECT_PORT))
        server.listen(30)
    
        print(f"Server started. Listening on {CORRECT_IP}:{CORRECT_PORT}")

        while True:
            conn, address = server.accept()
            #start new thread for each user that connects
            user_thread = threading.Thread(target = handle_user, args = (conn, address))
            user_thread.start()
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        server.close()

#Start the server with IP and port
start_server()
