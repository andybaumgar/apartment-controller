import asyncio
from kasa import SmartPlug
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()


def hours_to_seconds(seconds):
    return seconds * 60 * 60


async def control_loop(smart_plug):
    while True:
        await smart_plug.turn_off()
        print("AC turned on")
        sleep(hours_to_seconds(4))
        await smart_plug.turn_off()
        print("AC turned off")
        sleep(hours_to_seconds(0.5))


def run():
    smart_plug = SmartPlug(os.environ.get("PLUG_IP"))
    print("Connected to smart plug")
    print("Starting control loop")
    control_loop(smart_plug)


if __name__ == "__main__":
    run()
