import socket
import threading
host = '127.0.0.1' # local host
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} Leaves The Chat....!'.encode('ascii'))
            nicknames.remove(nickname)
            break
def recive():
    while True:
        client,address = server.accept()
        print(f'The Client {str(address)} is Connected...!')
        client.send('NickName : '.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f'Nickname of client:{address} is {nickname}..!')
        broadcast(f'-------{nickname} joins the Chat---------'.encode('ascii'))
        client.send('Connected to the Server'.encode('ascii'))
        thread_go = threading.Thread(target=handle,args=(client,))
        thread_go.start()
print('Server is Listning....')
recive()
