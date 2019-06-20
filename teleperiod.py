#!/usr/bin/env python
# This scirpt is used to change the telemetry period to 10 seconds instead of the 300 seconds used by default

import paho.mqtt.client as mqtt, sys
import time


# main
def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.is_connected = True

def on_message(client, userdata, message):
    ''' note: message is a tuple of (topic, payload, qos, retain)'''
    print("Got a message with topic [" + message.topic + "] and payload [" + str(message.payload) + "]" )

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.is_connected = False
client.loop_start()
client.connect("arupiot.com")

time.sleep(6)
if not client.is_connected:
    print("problem connecting to the MQTT server; please check your settings")
    sys.exit(1)

client.subscribe("project/sonoff/building/" + sys.argv[1] + "/power/stat/#")
client.publish("project/sonoff/building/" + sys.argv[1] + "/power/cmnd/TelePeriod", "10")

time.sleep(1)

client.loop_stop()
client.disconnect()
