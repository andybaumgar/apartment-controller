import os
from time import sleep

from dotenv import load_dotenv
from kasa import SmartPlug

from apartment_controller import config
from apartment_controller.utils.async_utils import async_to_sync
from apartment_controller.utils.time_utils import sleep_hours

load_dotenv()


@async_to_sync
async def turn_off_ac(smart_plugs):
    for smart_plug in smart_plugs:
        await smart_plug.turn_off()
    print("AC turned off")


@async_to_sync
async def turn_on_ac(smart_plugs):
    for smart_plug in smart_plugs:
        await smart_plug.turn_on()
    print("AC turned on")


def run():
    print("Running AC controller")
    ac_smart_plug = SmartPlug(config.ac_plug_ip)
    fan_smart_plug = SmartPlug(config.ac_fan_ip)
    smart_plugs = [ac_smart_plug, fan_smart_plug]
    print("Connected to smart plug")

    while True:
        turn_off_ac(smart_plugs)
        sleep_hours(0.75)
        print("starting sleep")
        turn_on_ac(smart_plugs)
        print("starting sleep")
        sleep_hours(4)


if __name__ == "__main__":
    ac_smart_plug = SmartPlug(config.ac_plug_ip)
    fan_smart_plug = SmartPlug(config.ac_fan_ip)
    smart_plugs = [ac_smart_plug, fan_smart_plug]
    # run()
    turn_off_ac([ac_smart_plug, fan_smart_plug])
