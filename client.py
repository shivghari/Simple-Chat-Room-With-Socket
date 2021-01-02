import socket
import threading
host = '127.0.0.1'
port = 55555
nickname = input('Enter Name : ')
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def recive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NickName : ':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('There Is an Error In Connection process!')
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

Thread_recv = threading.Thread(target=recive)
Thread_recv.start()
Thread_write = threading.Thread(target=write)
Thread_write.start()
