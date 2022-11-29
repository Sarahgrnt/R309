import socket
from _thread import *
msg=""
test=""
if __name__ =="__main__":
    server_socket = socket.socket()
    ThreadCount = 0

    try:
        #server_socket.bind(("127.0.0.1", 10000))
    #print('serveur démaré')
    except socket.error:
        print(str(socket.error))
    print('Socket is listening..')
    server_socket.listen(5)


    def multi_threaded_client(connection):
        connection.send(str.encode('Server is working:'))
        while True:
            data = connection.recv(2048)
            response = 'Server message: ' + data.decode('utf-8')
            if not data:
                 break
            connection.sendall(str.encode(response))
        connection.close()


    while True:
        Client, address = server_socket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(multi_threaded_client, (Client,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    server_socket.close()





