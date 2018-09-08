import serial
import MySQLdb
import os
import time
import datetime


import RPi.GPIO as GPIO

db = MySQLdb.connect(host="localhost",user="root",passwd="123",db="finger")
cur = db.cursor()
ser = serial.Serial('/dev/ttyUSB0',9600)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

while 1:
    s = ser.readline()
    if s=="fan":
        print("fan on....")
        GPIO.output(40, GPIO.HIGH)
    if s=="light":
        GPIO.output(38, GPIO.HIGH)
        
    if s=="fanout":
        GPIO.output(40, GPIO.LOW)
    if s=="lightout":
        GPIO.output(38, GPIO.HIGH)
