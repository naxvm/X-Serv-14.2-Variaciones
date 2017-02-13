#! /usr/bin/python3

# Aplicación web que devuelva siempre la misma página HTML,
# que tendrá que tener al menos una imagen (usando un elemento IMG).


import socket



mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1235))

mySocket.listen(5)


<<<<<<< HEAD
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:', recvSocket.recv(1024))
        recvSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n' +
                        '<html><body><h1>Hello World!' +
                        '<img src="http://2.bp.blogspot.com/_63jCiXixFMk/R8xviDmjAII/AAAAAAAAAGQ/vgU_rFcyVO0/S1600-R/gsyc.jpg"></h1></body></html>' +
                        '\r\n', 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print('Closing binded socket')
    mySocket.close()
=======

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print('HTTP request received:', recvSocket.recv(1024))
    recvSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n' +
                    '<html><body><h1>Sirviendo la imagen: <br><img src="http://2.bp.blogspot.com/_63jCiXixFMk/R8xviDmjAII/AAAAAAAAAGQ/vgU_rFcyVO0/S1600-R/gsyc.jpg"></h1></body></html>' +
                    '\r\n', 'utf-8'))
    recvSocket.close()
>>>>>>> c67bffd2ac150e4383a5a2d92d9aadc64ab85ad8
