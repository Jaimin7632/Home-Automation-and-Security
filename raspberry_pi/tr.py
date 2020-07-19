import sys
import socket
import os
import MySQLdb
db = MySQLdb.connect("localhost","root","123","iot")
cur = db.cursor()

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
            db1 = MySQLdb.connect(host="208.91.198.197",user="srpeciot",passwd="Abc@12345",db="iot")
            cur1 = db1.cursor()
            cur.execute("SELECT net FROM main where id=1")
            row=cur.fetchone()
            net =row[0]
            if net==1:
                cur.execute("SELECT * FROM main where id=1")
                row=cur.fetchone()
                net =row[6]
                fan =row[1]
                light =row[2]
                ac =row[3]
                projector =row[4]
                auto=row[5]
                door=row[7]
                cur.execute("UPDATE main SET net=0 WHERE id=1")
                
                cur1.execute("UPDATE main SET fan=%s WHERE id=1",(fan))
                cur1.execute("UPDATE main SET light=%s WHERE id=1",(light))
                cur1.execute("UPDATE main SET ac=%s WHERE id=1",(ac))
                cur1.execute("UPDATE main SET projector=%s WHERE id=1",(projector))
                cur1.execute("UPDATE main SET auto=%s WHERE id=1",(auto))
               # cur1.execute("UPDATE main SET door=%s WHERE id=1",(door))
            else:
                
                cur1.execute("SELECT * FROM main where id=1")
                row=cur1.fetchone()
                net =row[6]
                fan =row[2]
                light =row[1]
                ac =row[3]
                projector =row[4]
                auto=row[5]
                door=row[7]
                cur.execute("UPDATE main SET fan=%s WHERE id=1",(fan))
                cur.execute("UPDATE main SET light=%s WHERE id=1",(light))
                cur.execute("UPDATE main SET ac=%s WHERE id=1",(ac))
                cur.execute("UPDATE main SET projector=%s WHERE id=1",(projector))
                cur.execute("UPDATE main SET auto=%s WHERE id=1",(auto))
                #cur.execute("UPDATE main SET door=%s WHERE id=1",(door))
