#import numpy as np
import paho.mqtt.client as mqtt

MQTT_HOST="52.117.73.211"
MQTT_HOST="mqtt.eclipse.org"
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
    mqttclient.publish(MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)
mqttclient.on_message = on_message

# go into a loop
mqttclient.loop_forever()
