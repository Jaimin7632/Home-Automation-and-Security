import serial
import MySQLdb
import os
import time
import datetime
import glob
from time import strftime
db = MySQLdb.connect(host="localhost",user="root",passwd="123",db="finger")
cur = db.cursor()
ser = serial.Serial('/dev/ttyUSB0',9600)
while 1:
    read_serial=ser.readline()
    s = ser.readline()
    print s
    b="A"
    s1=len(s)
    print s1
    if s1 == 6:
        s=s[:4]
        print s
        DATE1 = (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
        print DATE1
        cur.execute("INSERT INTO main1 (id, date1) VALUES (%s ,%s)" , (s, DATE1))
        db.commit()
    else:
        print "play again.. etc..."
    
db.close()
