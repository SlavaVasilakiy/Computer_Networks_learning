# Task №2

Видео с практикой (https://disk.yandex.ru/i/uXIIMwm32thOJQ) <br>
команды для Cisco IOS - https://disk.yandex.ru/d/PwxEU3KrArG8Zw <br>

Условие: <br>
1) Настроить сеть согласно схеме в файле https://disk.yandex.ru/d/1m4aUoqDm1SKBQ
2) Проверить работоспособность соседних между собой сетей командой ping.
3) Обвести синим все broadcast домены <br>
   4*. Настроить loopback интерфейсы. <br>
   Скинуть скриншоты: <br>
   с зелеными линками <br>
   успешные пинги между парой-тройкой соседних сетей (соседние сети - это Connected сети к одному роутеру) <br>
   вывод любой таблицы ARP <br>

(Задание со * являются заданиями с повышенной сложностью и требуют самостоятельного изучения. <br>
Если они не выполнены, это не влияет на оценку)

# Solution:

1) Поднял все порты на роутерах, прописал для всех соответствующие IP и маски [s2.1_homework.pkt](s2.1_homework.pkt) <br>
![Homework_1_1.jpg](Homework_1_1.jpg)

2) Прописал статику на всех роутерах. <br>
![Homework_2_1.jpg](Homework_2_1.jpg)

3) Синие кружочки видно на первом скриншоте.

4) Поднял loopback интерфейсы на указанных роутерах, и пути к ним. <br>
![Homework_4_1.jpg](Homework_4_1.jpg) <br>
![Homework_4_2.jpg](Homework_4_2.jpg) <br>
Например пинг до loopback0 - 172.16.0.1/16 <br>
![Homework_4_3.jpg](Homework_4_3.jpg) <br>

ARP таблица <br>
![Homework_4_4.jpg](Homework_4_4.jpg)