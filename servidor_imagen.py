#! /usr/bin/python3

# Aplicación web que devuelva siempre la misma página HTML,
# que tendrá que tener al menos una imagen (usando un elemento IMG).


import socket



mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1235))

mySocket.listen(5)


try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:', recvSocket.recv(1024))
        recvSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n' +
                        '<html><body><h1>Hello World!</h1>' +
                        '<img src="https://assets.pcmag.com/media/images/532520-pangolin-v-day-google-doodle.jpg?thumb=y&width=810&height=455"></body></html>' +
                        '<img src="http://www.oasisinet.com/wp-content/uploads/2013/11/facebook-logo.jpg">' +                              
                        '\r\n', 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print('Closing binded socket')
    mySocket.close()

