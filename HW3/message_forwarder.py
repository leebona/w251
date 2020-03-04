#import numpy as np
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="mqtt-broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"

#REMOTE_MQTT_HOST="52.117.73.211"
REMOTE_MQTT_HOST="mqtt.eclipse.org"
REMOTE_MQTT_PORT=1883
REMOTE_MQTT_TOPIC="faces"

def on_connect(client, userdata, flags, rc):
  print("connected to broker with rc: " + str(rc))
  client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client,userdata, msg):
  try:
    print("message received!")
    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
    print("message published!")
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)

local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
