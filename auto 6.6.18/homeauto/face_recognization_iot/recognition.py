# 
#	recognition.py
#	Created by Dmitry Chulkov
#	This file provides set of functions that allow to detect faces on multiple images at one time,
#       add multiple faces to person and get name of person on image.
#

import Person
import PersonGroup
import Face
import getImage
import ftplib
#import RPi.GPIO as GPIO
import os
import json
import time
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(29, GPIO.OUT)

# this function addes faces to specified person in specified group.
# to do this you have to provide folder with images of person that you want to add,
# all images have to have only one face and this face have to be face of specified person.
# It's better to prepare special folder with such images and then proceed with this function.
def addFacesToPerson(folderWithImages, personID, personGroupID):

    files = os.listdir(folderWithImages)
    
    for i in range(len(files)):
        img_addr = folderWithImages + files[i]
        result = Person.addPersonFace(personGroupID, personID, img_addr)
        if "error" in result:
            print(json.dumps(result, indent=2))
        else:
            print("Added " + str(i+1) + " faces... ")
    print("Done adding faces!")
    return

# Function prints out json in readable format        
def printResJson(result):
    print(json.dumps(result, indent=2))
    return

# using module 'Face' and function 'detect' print out result of detecting faces on
# on images in specified directory
def detectFaceOnImages(path):
    files = os.listdir(path)
    for i in range(len(files)):
        img_addr = path + files[i]
        result = Face.detect(img_addr)
        print("*************")
        print("image: " + img_addr)
        printResJson(result)
    return


# params: path to image example\\example\\
def checkPerson(image, personGroupID):
    
    # detect face 
    result = Face.detect(image)
    if len(result) > 0 and 'faceId' in result[0]:
        data = Face.identify([result[0]['faceId']], personGroupID)
        # get person name
        
        if len(data[0]["candidates"]) > 0:
            persID = data[0]["candidates"][0]["personId"]
            res = Person.getPerson(personGroupID, persID)
            name = res["name"]
            #GPIO.output(29,GPIO.HIGH)            
            time.sleep(7)
            #GPIO.output(29,GPIO.LOW)
    
        else:
            name = "stranger"
            session = ftplib.FTP('srpec.org.in','iot','Abc@12345')
            file = open('/home/pi/image.jpg','rb')
# file to send

            session.storbinary('STOR img.jpg', file)     # send the file
            file.close()                                    # close file and FTP
            session.quit()
        return name
    else:
        print("No face detected")
    return "noface"




path = "D:/"
host = "192.168.43.1:8080"

    # save a picture of a violator
#getImage.fromIpCam(path, host)
    # get name of person on the photo
name = checkPerson(path + "image.jpg", "vvv-vvv")
print(name)



