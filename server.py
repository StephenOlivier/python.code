import socket
import threading

# Constants for the server
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on
clients = []

# Function to handle each client connection
def handle_client(client_socket, addr):
    print(f"[INFO] Client connected from {addr}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[INFO] Received from {addr}: {message}")
                broadcast(message, client_socket)  # Send the message to all clients
            else:
                remove(client_socket)
                break
        except:
            continue

# Function to broadcast a message to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

# Function to remove a client that has disconnected
def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Server setup
def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[INFO] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

if __name__ == "__main__":
    server_program()
