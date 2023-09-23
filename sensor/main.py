import time
import machine
import onewire, ds18x20
import json

with open("config.json","r") as file:
    global data
    data = json.load(file)

temperature_pin = machine.Pin(data['pin'])
read_interval = data['interval']

temp = ds18x20.DS18X20(onewire.OneWire(temperature_pin))

roms = temp.scan()

while True:
    temp.convert_temp()
    time.sleep_ms(read_interval)
    print('temperature:', end=' ')
    for rom in roms:
        print(temp.read_temp(rom), end='\n')
        json.load
