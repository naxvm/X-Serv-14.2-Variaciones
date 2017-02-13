#! /usr/bin/python3

# Aplicación web que devuelva un código de error 404 y muestre un mensaje
# en el navegador.


import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1235))

mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received', recvSocket.recv(1024))
        recvSocket.send(bytes('HTTP/1.1 404 Not Found\r\n\r\n' +
                        '<html><head><title>P&aacute;gina no encontrada</title></head>' +
                        '<body>Revisa tu URL, por favor.</p1></body></html>' +
                        '\r\n', 'utf-8'))

        recvSocket.close()
except KeyboardInterrupt:
        print('Closing binded socket')
        mySocket.close()
