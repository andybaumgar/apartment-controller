from kasa import SmartPlug
from dotenv import load_dotenv
import os
from apartment_controller.async_utils import async_to_sync
from time import sleep

load_dotenv()


def sleep_hours(seconds):
    sleep(seconds * 60 * 60)


@async_to_sync
async def turn_off_ac(smart_plug):
    await smart_plug.turn_off()
    print("AC turned off")


@async_to_sync
async def turn_on_ac(smart_plug):
    await smart_plug.turn_on()
    print("AC turned on")


def run():
    smart_plug = SmartPlug(os.environ.get("AC_PLUG_IP"))
    print("Connected to smart plug")

    while True:
        turn_on_ac(smart_plug)
        sleep_hours(4)
        turn_off_ac(smart_plug)
        sleep_hours(0.5)


if __name__ == "__main__":
    run()
