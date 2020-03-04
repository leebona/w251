import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt
import calendar
import time

MQTT_HOST="mqtt-broker"
MQTT_PORT=1883
MQTT_TOPIC="faces"

def on_connect(client, userdata, flags, rc):
  print("connected to broker with rc: " + str(rc))
  client.subscribe(MQTT_TOPIC)

def on_message(client,userdata, msg):
  try:
    print("message received!")
    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    temp = np.frombuffer(msg, dtype='uint8')
    img = cv.imdecode(temp, flags=1)
    name = "/mnt/mybucket/image-"+str(round(time.time()))
    cv.imwrite(name, img)
  except:
    print("Unexpected error:", sys.exc_info()[0])

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)
mqttclient.on_message = on_message

# go into a loop
mqttclient.loop_forever()
