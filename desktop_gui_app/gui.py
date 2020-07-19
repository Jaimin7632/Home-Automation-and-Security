
import socket
import time
import sys
import os
import pymysql
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

while 1:
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
            
    def checkserver():    
        if internet_on()==1:
            db = pymysql.connect(host="208.91.198.197",user="srpeciot",passwd="Abc@12345",db="iot")
            cur = db.cursor()
            
        else:
            db = pymysql.connect("localhost","root","123","iot")
            cur = db.cursor()
            cur.execute("UPDATE main SET net=1 WHERE id=1")
        return cur   
    class App(QWidget):
             
                    def __init__(self):
                        super().__init__()
                        self.title = 'HOME AUTO'
                        self.left = 0
                        self.top = 1
                        self.width = 1060
                        self.height = 600
                        self.initUI()
             
                    def initUI(self):
                        self.setWindowTitle(self.title)
                        self.setGeometry(self.left, self.top, self.width, self.height)
             
                        buttonmanual = QPushButton('MANUAL', self)
                        buttonmanual.move(300,100) 
                        buttonmanual.clicked.connect(self.manual)
                        buttonauto = QPushButton('AUTO', self)
                        buttonauto.move(600,100) 
                        buttonauto.clicked.connect(self.auto)
                        
                        button = QPushButton('FAN ON', self)
                        button.move(150,200) 
                        button.clicked.connect(self.fan)

                        button1 = QPushButton('FAN OFF', self)
                        button1.move(150,400) 
                        button1.clicked.connect(self.fanoff)

                        button2 = QPushButton('LIGHT ON', self)
                        button2.move(300,200) 
                        button2.clicked.connect(self.light)

                        button3 = QPushButton('LIGHT OFF', self)
                        button3.move(300,400) 
                        button3.clicked.connect(self.lightoff)

                        button4 = QPushButton('AC ON', self)
                        button4.move(450,200) 
                        button4.clicked.connect(self.ac)

                        button5 = QPushButton('AC OFF', self)
                        button5.move(450,400) 
                        button5.clicked.connect(self.acoff)

                        button6 = QPushButton('PROJECTOR ON', self)
                        button6.move(600,200) 
                        button6.clicked.connect(self.pr)

                        button7 = QPushButton('PROJECTOR OFF', self)
                        button7.move(600,400) 
                        button7.clicked.connect(self.proff)
             
                        self.show()
             
                    @pyqtSlot()
                    def auto(self):
                        cu=checkserver()
                        cu.execute("UPDATE main SET auto=1 WHERE id=1")
                        
                        
                    def manual(self):
                        cu=checkserver()
                        cu.execute("UPDATE main SET auto=0 WHERE id=1")
                        
                    def fan(self):
                        cu=checkserver()
                        cu.execute("SELECT auto FROM main WHERE id=1")
                        a=cu.fetchone()
                        ab=a[0]
                        if ab==0:
                            cu.execute("UPDATE main SET fan=1 WHERE id=1")
                            
                       
                    def fanoff(self):
                        cu=checkserver()
                        cu.execute("SELECT auto FROM main WHERE id=1")
                        a=cu.fetchone()
                        ab=a[0]
                        if ab==0:
                            cu.execute("UPDATE main SET fan=0 WHERE id=1")
                            
            
                    def light(self):
                        cu=checkserver()
                        cu.execute("SELECT auto FROM main WHERE id=1")
                        a=cu.fetchone()
                        ab=a[0]
                        if ab==0:
                            cu.execute("UPDATE main SET light=1 WHERE id=1")
                            

                    def lightoff(self):
                        cu=checkserver()
                        cu.execute("SELECT auto FROM main WHERE id=1")
                        a=cu.fetchone()
                        ab=a[0]
                        if ab==0:
                            cu.execute("UPDATE main SET light=0 WHERE id=1")
                            

                    def ac(self):
                        cu=checkserver()
                        cu.execute("SELECT auto FROM main WHERE id=1")
                        a=cu.fetchone()
                        ab=a[0]
                        if ab==0:
                            cu.execute("UPDATE main SET ac=1 WHERE id=1")
                            

                    def acoff(self):
                        cu=checkserver()
                        cu.execute("SELECT auto FROM main WHERE id=1")
                        a=cu.fetchone()
                        ab=a[0]
                        if ab==0:
                            cu.execute("UPDATE main SET ac=0 WHERE id=1")
                            

                    def pr(self):
                        cu=checkserver()
                        cu.execute("SELECT auto FROM main WHERE id=1")
                        a=cu.fetchone()
                        ab=a[0]
                        if ab==0:
                            cu.execute("UPDATE main SET projector=1 WHERE id=1")
                            
                        
                    def proff(self):
                        cu=checkserver()
                        cu.execute("SELECT auto FROM main WHERE id=1")
                        a=cu.fetchone()
                        ab=a[0]
                        if ab==0:
                            cu.execute("UPDATE main SET projector=0 WHERE id=1")
                        
                        

               
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
            
           
               
           
            
       
             
            
            
