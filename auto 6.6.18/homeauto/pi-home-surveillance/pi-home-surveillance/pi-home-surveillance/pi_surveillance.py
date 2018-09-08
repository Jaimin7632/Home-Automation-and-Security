# USAGE
# python pi_surveillance.py --conf conf.json

# import the necessary packages
from pyimagesearch.tempimage import TempImage
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import warnings
import socket
import datetime
import MySQLdb
import RPi.GPIO as GPIO
import imutils
import json
import time
import cv2


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
# construct the argument parser and parse the arguments

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

conf = json.load(open('conf.json'))
client = None

# check to see if the Dropbox should be used

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = tuple(conf["resolution"])
camera.framerate = conf["fps"]
rawCapture = PiRGBArray(camera, size=tuple(conf["resolution"]))

# allow the camera to warmup, then initialize the average frame, last
# uploaded timestamp, and frame motion counter
print("[INFO] warming up...")
time.sleep(conf["camera_warmup_time"])
avg = None
lastUploaded = datetime.datetime.now()
motionCounter = 0

# capture frames from the camera
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image and initialize
	# the timestamp and occupied/unoccupied text
	if internet_on()==1:
            db = MySQLdb.connect(host="208.91.198.197",user="srpeciot",passwd="Abc@12345",db="iot")
            cur = db.cursor()
            
        else:
            db = MySQLdb.connect("localhost","root","123","iot")
            cur = db.cursor()
            cur.execute("UPDATE main SET net=1 WHERE id=1")
	frame = f.array
	timestamp = datetime.datetime.now()
	text = "Unoccupied"

	# resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	# if the average frame is None, initialize it
	if avg is None:
		print("[INFO] starting background model...")
		avg = gray.copy().astype("float")
		rawCapture.truncate(0)
		continue

	# accumulate the weighted average between the current frame and
	# previous frames, then compute the difference between the current
	# frame and running average
	cv2.accumulateWeighted(gray, avg, 0.5)
	frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))

	# threshold the delta image, dilate the thresholded image to fill
	# in holes, then find contours on thresholded image
	thresh = cv2.threshold(frameDelta, conf["delta_thresh"], 255,
		cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]

	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < conf["min_area"]:
			continue

		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"

	# draw the text and timestamp on the frame
	ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.35, (0, 0, 255), 1)

	# check to see if the room is occupied
	if text == "Occupied":
		# check to see if enough time has passed between uploads

		cur.exexute("SELECT auto from main where id=1")
		auy=cur.fetchone()
		auto=auy[0]
		if auto ==1:
                        GPIO.output(40,GPIO.HIGH)
                        GPIO.output(36,GPIO.HIGH)
                        cur.execute('update main set fan=1,ac=1 where id=1')
                        lastfanon=timestamp
		
		if (timestamp - lastUploaded).seconds >= 5.0:
			# increment the motion counter
			motionCounter += 1
                        session = ftplib.FTP('srpec.org.in','iot','Abc@12345')
                        file = frame
                        session.storbinary('STOR img2.jpg', file)     # send the file
                        file.close()                                    # close file and FTP
                        session.quit()
			lastUploaded = timestamp
			motionCounter = 0
	# otherwise, the room is not occupied
	else:
		motionCounter = 0
		if (timestamp - lastfanon).seconds >= 10.0:
                        GPIO.output(40,GPIO.LOW)
                        GPIO.output(36,GPIO.LOW)
                        cur.execute('update main set fan=0,ac=0 where id=1')
		

	# check to see if the frames should be displayed to screen
	if conf["show_video"]:
		# display the security feed
		cv2.imshow("Security Feed", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key is pressed, break from the lop
		if key == ord("q"):
			break

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
