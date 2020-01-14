import time
import binascii
import RPi.GPIO as GPIO   
from time import sleep     
GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BOARD)   
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)   

pesan = input("masukan pesan: ")
pesan = str(pesan)

biner = bin(int.from_bytes(pesan.encode(), 'big'))
bin2list = biner[2:]
listbin = []
for i in bin2list:
    listbin.append(i)
listbin.insert(0,"0")
listbin.insert(0,"1")
for i in range(len(listbin)):
    nilai = listbin[i]
    if (nilai == "0"):
        GPIO.output(12, GPIO.LOW)
    if(nilai == "1"):
        GPIO.output(12, GPIO.HIGH)
    time.sleep(.001)
GPIO.output(12,GPIO.LOW)
