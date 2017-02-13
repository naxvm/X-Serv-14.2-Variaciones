#! /usr/bin/python3
# Aplicación web que produzca una redirección a la página http://gsyc.es/


import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1235))

mySocket.listen(5)


try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received: ', recvSocket.recv(1024))
        recvSocket.send(bytes("HTTP/1.1 301 Moved Permanently\r\nLocation: http://gsyc.es\r\n\r\n" +
                              "<html><head><title>REDIRIGIENDO</title></head>" +
                              "<body>Este texto no se mostrara, pero la pagina ha cambiado de direccion</body></html>", 'utf-8'))


        recvSocket.close()


except KeyboardInterrupt:
    print('Closing binded socket')
    mySocket.close()
