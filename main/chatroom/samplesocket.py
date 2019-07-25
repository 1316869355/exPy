import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 56661))
sk.listen(5)

conn, address = sk.accept()
sk.sendall(bytes('hello world', encoding='utf-8'))
