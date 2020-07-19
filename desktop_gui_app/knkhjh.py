import os
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
            
        
    if internet_on()==1:
        db = pymysql.connect("localhost","root","123","iot")
        cur = db.cursor()
        print ("onnnn")
        os.system('python gui.py')
    else:
        db = pymysql.connect("localhost","root","123","iot")
        cur = db.cursor()
        print("offffff")
        os.system('python gui.py')
