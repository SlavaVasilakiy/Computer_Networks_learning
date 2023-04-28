#!/bin/python3

# импортирование модуля сокетов и модуля многопоточности
import socket
import threading

# данные для подключения
host = '192.168.2.19' # IP-адрес сервера
port = 55555         # номер порта, используемого сервером

# создание сокета сервера, привязка его к адресу и порту, и запуск прослушивания входящих соединений
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# создание списков для хранения подключенных клиентов и их ников
clients = []
nicknames = []

# функция для отправки сообщений всем клиентам
def broadcast(message):
    for client in clients:
        client.send(message)

# функция для обработки сообщений от клиентов
def handle(client):
    while True:
        try:
            # получение сообщения от клиента и его рассылка всем подключенным клиентам
            message = client.recv(1024)
            broadcast(message)
        except:
            # удаление клиента и закрытие соединения в случае ошибки и выход из функции
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} покинул чат!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

# функция для прослушивания входящих соединений
def receive():
    while True:
        # принятие входящего подключения
        client, address = server.accept()
        print("Подключен {}".format(str(address)))

        # запрос и сохранение ника клиента
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # вывод и рассылка ника клиента всем подключенным клиентам
        print("Ник: {}".format(nickname))
        broadcast("{} присоединился к чату!".format(nickname).encode('ascii'))
        client.send('Подключено к серверу!'.encode('ascii'))

        # запуск отдельного потока для обработки сообщений от клиента
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Сервер запущен...")
receive()
