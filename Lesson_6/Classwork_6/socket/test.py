import socket
import threading
from time import sleep

ya_sock = socket.socket() # создаём сокет
addr = ("77.88.55.242", 443) # присваиваем IP и порт в переменную
ya_sock.connect(addr) # коннектимся по указанному адресу и порту

data_out = b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n" # HTTP запрос
ya_sock.send(data_out) # шлём запрос

data_in = b"" # создаём переменную для сбора информации

def recieving(): # функция с циклом на сбор информации в буфера и записью из буферов в переменную
    global data_in
    while True:
        data_chunk = ya_sock.recv(1024)
        data_in += data_chunk

rec_thread = threading.Thread(target=recieving) # создаём поток с функцией сбора информации
rec_thread.start() # запускаем поток

sleep(4) # выставляем задержку 4 секунды, что бы информация успела записаться
print(data_in) # выводим все данные в печать

ya_sock.close() # закрываем соединение
