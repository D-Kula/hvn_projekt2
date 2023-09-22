import onewire
import ds18x20
import time
import json
import paho.mqtt.client as mqtt

data = 0

with open("config.json","r") as file:
    data = file

temperature_pin = data['pin']
read_interval = data['interval']





client = mqtt.Client()