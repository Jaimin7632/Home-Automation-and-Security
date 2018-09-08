import serial
import socket
import MySQLdb
import os
import time
import datetime
import glob
from time import strftime

import RPi.GPIO as GPIO
from threading import Thread

class waiter(Thread):
    def run(self):
        GPIO.output(29,GPIO.HIGH)
        time.sleep(7)
        GPIO.output(29,GPIO.LOW)
           
            



GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
db1 = MySQLdb.connect("localhost","root","123","iot")
cur1 = db1.cursor()
def internet_on():
        
        try:
            host=socket.gethostbyname("www.google.com")
            s=socket.create_connection((host,80),2)
            s.close()
            print ("ion")
            return 1
        except Exception:
            print("ioff")
            return 0
        
            
    
while 1:

        
    if internet_on()==1:
            db = MySQLdb.connect(host="208.91.198.197",user="srpeciot",passwd="Abc@12345",db="iot")
            cur = db.cursor()
            
    else:
            db = MySQLdb.connect("localhost","root","123","iot")
            cur = db.cursor()
            cur.execute("UPDATE main SET net=1 WHERE id=1")
          




    cur.execute("SELECT auto,door FROM main where id=1")
    aut=cur.fetchone()
    at=aut[0]

    door=aut[1]
    if door==1:
            waiter().start()
            cur.execute("UPDATE main SET door=0 WHERE id=1")

    if at==0:
        GPIO.output(37,GPIO.LOW)
        cur.execute("SELECT fan,light,ac,projector FROM main where id=1")
        row=cur.fetchone()
        fan =row[0]
        light =row[1]
        ac =row[2]
        projector =row[3]
        if fan==1:
            print("fan on")
            GPIO.output(40,GPIO.HIGH)
        else :
            print("fan off")
            GPIO.output(40,GPIO.LOW)
        if light==1:
            print("light on")
            GPIO.output(38,GPIO.HIGH)
        else :
            print("light off")
            GPIO.output(38,GPIO.LOW)
        if ac==1:
            print("ac on")
            GPIO.output(36,GPIO.HIGH)
        else :
            print("ac off")
            GPIO.output(36,GPIO.LOW)
        if projector==1:
            print("pr on")
            GPIO.output(32,GPIO.HIGH)
        else :
            print("pr off")
            GPIO.output(32,GPIO.LOW)
    else :  #auto work
        GPIO.output(37,GPIO.HIGH)
        #day = time.strftime("%A")
        #hr = time.strftime("%H")
        #mi = time.strftime("%M")
        day="Monday"
        hr=9
        mi=50
        sr = "SELECT "+str(day)+" FROM timetable"
        cur1.execute(sr)
        et=cur1.fetchone()        
        one = et[0]
        et=cur1.fetchone()        
        two = et[0]
        et=cur1.fetchone()        
        three = et[0]
        et=cur1.fetchone()        
        four = et[0]
        et=cur1.fetchone()        
        five = et[0]
        et=cur1.fetchone()        
        six = et[0]
        if one==1:
            if hr==8 and mi==45:
                GPIO.output(32,GPIO.HIGH)
                GPIO.output(36,GPIO.HIGH)
                cur.execute("UPDATE main SET ac=1 where id=1")
                cur.execute("UPDATE main SET projector=1 where id=1")
            if hr==9 and mi==49:
                GPIO.output(32,GPIO.LOW)
                GPIO.output(36,GPIO.LOW)
                cur.execute("UPDATE main SET ac=0 where id=1")
                cur.execute("UPDATE main SET projector=0 where id=1")
        if two==1:
            if hr==9 and mi==50:
                GPIO.output(32,GPIO.HIGH)
                GPIO.output(36,GPIO.HIGH)
                cur.execute("UPDATE main SET ac=1 where id=1")
                cur.execute("UPDATE main SET projector=1 where id=1")
            if hr==10 and mi==45:
                GPIO.output(32,GPIO.LOW)
                GPIO.output(36,GPIO.LOW)
                cur.execute("UPDATE main SET ac=0 where id=1")
                cur.execute("UPDATE main SET projector=0 where id=1")
           
        if three==1:
            if hr==11 and mi==30:
                GPIO.output(32,GPIO.HIGH)
                GPIO.output(36,GPIO.HIGH)
                cur.execute("UPDATE main SET ac=1 where id=1")
                cur.execute("UPDATE main SET projector=1 where id=1")
            if hr==12 and mi==24:
                GPIO.output(32,GPIO.LOW)
                GPIO.output(36,GPIO.LOW)
                cur.execute("UPDATE main SET ac=0 where id=1")
                cur.execute("UPDATE main SET projector=0 where id=1")
        if four==1:
            if hr==12 and mi==25:
                GPIO.output(32,GPIO.HIGH)
                GPIO.output(36,GPIO.HIGH)
                cur.execute("UPDATE main SET ac=1 where id=1")
                cur.execute("UPDATE main SET projector=1 where id=1")
            if hr==13 and mi==19:
                GPIO.output(32,GPIO.LOW)
                GPIO.output(36,GPIO.LOW)
                cur.execute("UPDATE main SET ac=0 where id=1")
                cur.execute("UPDATE main SET projector=0 where id=1")

        if five==1:
            if hr==13 and mi==30:
                GPIO.output(32,GPIO.HIGH)
                GPIO.output(36,GPIO.HIGH)
                cur.execute("UPDATE main SET ac=1 where id=1")
                cur.execute("UPDATE main SET projector=1 where id=1")
            if hr==14 and mi==24:
                GPIO.output(32,GPIO.LOW)
                GPIO.output(36,GPIO.LOW)
                cur.execute("UPDATE main SET ac=0 where id=1")
                cur.execute("UPDATE main SET projector=0 where id=1")
        if six==1:
            if hr==14 and mi==25:
                GPIO.output(32,GPIO.HIGH)
                GPIO.output(36,GPIO.HIGH)
                cur.execute("UPDATE main SET ac=1 where id=1")
                cur.execute("UPDATE main SET projector=1 where id=1")
            if hr==15 and mi==20:
                GPIO.output(32,GPIO.LOW)
                GPIO.output(36,GPIO.LOW)
                cur.execute("UPDATE main SET ac=0 where id=1")
                cur.execute("UPDATE main SET projector=0 where id=1")
        

        if(GPIO.input(11)):
            cur.execute("UPDATE main SET fan=0 where id=1")
            GPIO.output(40,GPIO.HIGH)
            
        else:
            cur.execute("UPDATE main SET fan=1 where id=1")
            GPIO.output(40,GPIO.LOW)
            

        if(GPIO.input(13)):
            cur.execute("UPDATE main SET light=0 where id=1")
            GPIO.output(38,GPIO.HIGH)
            
        else:
            cur.execute("UPDATE main SET light=1 where id=1")
            GPIO.output(40,GPIO.LOW)
            
            
            
            
            
            
            
           
                   
                   
               
        
        
