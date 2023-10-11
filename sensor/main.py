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


def get_id_hex(rom):
    return f"{hex(int.from_bytes(rom,'little'))[2:]}"


while True:
    temp.convert_temp()
    time.sleep_ms(read_interval)
    for rom in roms:
        print(
            f"{unit_id[2:]}" + " " + get_id_hex(rom),
            end=" ",
        )
        print(temp.read_temp(roms[0]), end="\n")
