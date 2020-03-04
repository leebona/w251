import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt
import time

face_cascade = cv.CascadeClassifier('/tmp/hw3/haarcascade_frontalface_default.xml')

MQTT_HOST="mqtt-broker"
MQTT_PORT=1883
MQTT_TOPIC="faces"

def on_connect(client, userdata, flags, rc):
  print("connected to broker with rc: " + str(rc))

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard cameracap = cv2.VideoCapture(0)
cap = cv.VideoCapture(1)

mqttclient.loop_start()
time.sleep(1)

while(True):
  # Capture frame-by-frame
  ret, frame = cap.read()
  # We don't use the color information, so might as well save space
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  # face detection and other logic goes here
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    # your logic goes here; for instance
    # cut out face from the frame..
    cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    face = gray[y:y+h,x:x+w]
    rc,png = cv.imencode('.png', face)
    msg = png.tobytes()
    mqttclient.publish(MQTT_TOPIC, msg, qos=0, retain=False)

time.sleep(1)
mqttclient.loop_end()
mqttclient.disconnect()
