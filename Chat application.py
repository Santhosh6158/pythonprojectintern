import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Connection established with {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Client {client_address}: {message}")
                client_socket.send("Message received".encode())
            else:
                break
        except:
            print(f"Connection closed by {client_address}")
            break
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8080))
    server_socket.listen(5)
    print("Server started, waiting for connections...")
    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Server: {message}")
        except:
            print("Connection closed by the server")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8080))
    print("Connected to the server. Type your messages below:")
    
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    while True:
        message = input()
        if message.lower() == "exit":
            break
        client_socket.send(message.encode())
    client_socket.close()

if __name__ == "__main__":
    mode = input("Enter 'server' to start as server or 'client' to start as client: ").lower()
    if mode == "server":
        start_server()
    elif mode == "client":
        start_client()
    else:
        print("Invalid mode. Please restart and choose 'server' or 'client'.")