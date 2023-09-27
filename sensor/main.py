import time
import machine
import onewire, ds18x20
import json

with open("config.json", "r") as file:
    global data
    data = json.load(file)

temperature_pin = machine.Pin(data["pin"])
read_interval = data["interval"]

temp = ds18x20.DS18X20(onewire.OneWire(temperature_pin))

roms = temp.scan()

unit_id = hex(int.from_bytes(machine.unique_id(), "little"))
sensor_id = hex(int.from_bytes(roms[0], "little"))

while True:
    temp.convert_temp()
    time.sleep_ms(read_interval)
    print(f"{unit_id[2:]}" + " " + f"{sensor_id[2:]}", end=" ")
    print(temp.read_temp(roms[0]), end="\n")
