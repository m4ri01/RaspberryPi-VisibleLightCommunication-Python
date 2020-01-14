import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
tampung = []
nilainull = 0
ns = 0
jumkar = 1
kartampung = []
while True:
    kondisi =   GPIO.input(11)
    time.sleep(.001)
    if kondisi == 1:
        while True:
            angka = GPIO.input(11)
            tampung.append(angka)
            if angka == 0:
               nilainull = nilainull +1
            if angka == 1:
               nilainull = 0
            if nilainull >=16:
                jumkar = len(tampung) / 8
                kar = int(jumkar)
                jumkar = 8*kar
                tampung = tampung[0:jumkar]
                ba = 8
                bb = 0
                for i in range (0,kar):
                    tampungtemp = tampung[bb:ba]
                    hasil = "".join(str(x) for x in tampungtemp)
                    hasil = int(hasil,2)
                    karasli = str(chr(hasil))
                    kartampung.append(karasli)
                    ba = ba + 8
                    bb = bb + 8
                try:
                    kartampung.remove("\x00")
                except:
                    pass
#                print(tampung)
                pesanterima = "".join(str(x) for x in kartampung)
                print("pesan diterima = {}".format(pesanterima))
                tampung=[]
                kartampung=[]
                sys.exit()
            time.sleep(.001)

