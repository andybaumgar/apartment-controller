from kasa import SmartPlug
from dotenv import load_dotenv
import os
from apartment_controller.utils.async_utils import async_to_sync
from apartment_controller.utils.time_utils import sleep_hours
from time import sleep
from apartment_controller import config

load_dotenv()


@async_to_sync
async def turn_off_ac(smart_plug):
    await smart_plug.turn_off()
    print("AC turned off")


@async_to_sync
async def turn_on_ac(smart_plug):
    await smart_plug.turn_on()
    print("AC turned on")


def run():
    print("Running AC controller")
    smart_plug = SmartPlug(config.ac_plug_ip)
    print("Connected to smart plug")

    while True:
        turn_off_ac(smart_plug)
        sleep_hours(0.75)
        print("starting sleep")
        turn_on_ac(smart_plug)
        print("starting sleep")
        sleep_hours(4)


if __name__ == "__main__":
    run()
