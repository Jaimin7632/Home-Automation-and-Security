# -*- coding: utf-8 -*-
import serial
import MySQLdb
import os
import time
import datetime
import glob
from time import strftime
db = MySQLdb.connect(host="localhost",user="root",passwd="123",db="iot")
cur = db.cursor()
ser = serial.Serial('/dev/ttyUSB0',9600)
while 1:
    read_serial=ser.readline()
    s = ser.readline()

    s1=len(s)
    som="someone try to open your lock"
    if s1==11:
        cur.execute("INSERT INTO notify(msg,flag) VALUES (%s,1)",(som))
        
    if s1==6:
        cur.execute("UPDATE main set auto=1")
        
db.close()
