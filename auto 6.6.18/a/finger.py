# -*- coding: utf-8 -*-
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
    b="A"
    s1=len(s)
    print ("###############")
    if s1 == 6:
        s=s[:4]
        print s
        cur.execute("SELECT * FROM detail where id=%s",(s))
        row = cur.fetchone()
        d=row[3]    #d flag
        DATE1 = time.strftime("%Y-%m-%d")
        #DATE1='2017-10-22'
        cur.execute("INSERT INTO temp (date1) VALUES (%s)" , (DATE1))
        cur.execute("SELECT date1 FROM temp")
        row3 = cur.fetchone()
        DATE2 = row3[0]
        cur.execute("TRUNCATE TABLE temp")
        
        cur.execute("SELECT date1 FROM detail where id=%s",(s))
        row = cur.fetchone()
        dd = row[0]
        TIME = time.strftime("%H:%M")
        #TIME = "17:45"
        #hr="17"
        #mi="45"
        hr = time.strftime("%H")
        mi = time.strftime("%M")
        cur.execute("SELECT * FROM detail where id=%s",(s))
        row = cur.fetchone()
        d=row[3]
        print DATE2
        print TIME
        if DATE2 != dd and d==1:
            cur.execute("UPDATE detail set flag=0 where id=%s",(s))
            cur.execute("DELETE from temp1 where id=%s",(s))
            d=0
           
            
                 
        if d==0:
            print("IN ENTRY....")
            cur.execute("INSERT INTO main1 (id, date1,time,flag) VALUES (%s ,%s,%s,%s)" , (s, DATE2,TIME,d))
            cur.execute("UPDATE detail set date1=%s where id=%s",(DATE2,s))
            cur.execute("UPDATE detail set flag=1 where id=%s",(s))
            cur.execute("INSERT INTO temp1(whr,wmi,id) VALUES (%s,%s,%s)",(hr,mi,s))
        else:
            print("OUT ENTRY...")
            cur.execute("INSERT INTO main1 (id, date1,time,flag) VALUES (%s ,%s,%s,%s)" , (s, DATE2,TIME,d))
            cur.execute("UPDATE detail set flag=0 where id=%s",(s))
            cur.execute("INSERT INTO temp2(whr,wmi,id) VALUES (%s,%s,%s)",(hr,mi,s))
            cur.execute("UPDATE detail set date1=%s where id=%s",(DATE2,s))
            cur.execute("SELECT * from temp1")
            ew = cur.fetchone()
            oldhr=ew[0]
            oldmi=ew[1]
            cur.execute("SELECT * from temp2")
            ew = cur.fetchone()
            newhr=ew[0]
            newmi=ew[1]
            mhr=int(newhr)-int(oldhr)
            mmi=int(newmi)-int(oldmi)
            print("*****")
            print(mhr)
            print(mmi)
            print("*****")
            if mmi<0:
                mmi=60+mmi
                mhr=mhr-1
            cur.execute("SELECT * from dtw where id=%s AND date1=%s",(s,DATE2))
            if cur.rowcount==0:
                cur.execute("INSERT INTO dtw(id,date1,whr,wmi) VALUES (%s,%s,%s,%s)",(s,DATE2,mhr,mmi))
            else:
                tr=cur.fetchone()
                ohr=tr[2]
                omi=tr[3]
                shr=int(ohr)+int(mhr)
                smi=int(omi)+int(mmi)
                while smi>60:
                    smi=smi-60
                    shr=shr+1
                cur.execute("UPDATE dtw set whr=%s where id=%s AND date1=%s",(shr,s,DATE2))
                cur.execute("UPDATE dtw set wmi=%s where id=%s AND date1=%s",(smi,s,DATE2))
            cur.execute("DELETE from temp1 where id=%s",(s))
            cur.execute("DELETE from temp2 where id=%s",(s))
            cur.execute("SELECT thr,tmi from detail where id=%s",(s))
            qe = cur.fetchone()
            thr=qe[0]
            tmi=qe[1]
            tthr=int(thr)+int(mhr)
            ttmi=int(tmi)+int(mmi)
            while ttmi> 60:
                ttmi=ttmi-60
                tthr=tthr+1
            cur.execute("UPDATE detail set tmi=%s where id=%s",(ttmi,s)) 
            cur.execute("UPDATE detail set thr=%s where id=%s",(tthr,s))   
        db.commit()
    else:
        print "play again.. etc..."
    
db.close()
