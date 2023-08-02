from kasa import SmartPlug
from apartment_controller.utils.async_utils import async_to_sync
from time import sleep
import asyncio
from apartment_controller.utils.time_utils import sleep_minutes, is_asleep, is_dark_out
from typing import List
from apartment_controller import config


@async_to_sync
async def turn_on_lights(smart_plugs):
    print("Turning on lights")
    tasks = [smart_plug.turn_on() for smart_plug in smart_plugs]
    try:
        await asyncio.gather(*tasks)
    except Exception as e:
        print(e)
    print("Lights turned on")


@async_to_sync
async def turn_off_lights(smart_plugs):
    tasks = [smart_plug.turn_off() for smart_plug in smart_plugs]
    try:
        await asyncio.gather(*tasks)
    except Exception as e:
        print(e)
    print("Lights turned off")


def run(lights_on=False):
    print("Running light controller")
    smart_plugs = [SmartPlug(ip) for ip in config.light_plug_ips]
    is_dark_out = is_dark_out(sunset_offset=config.sunset_offset)

    while True:
        # if not lights_on and is_dark_out() and not is_asleep():
        if is_dark_out and not is_asleep():
            turn_on_lights(smart_plugs)
            lights_on = True
            print("starting sleep")
        # elif lights_on and (not is_dark_out() or is_asleep()):
        elif not is_dark_out or is_asleep():
            turn_off_lights(smart_plugs)
            lights_on = False
            print("starting sleep")

        sleep_minutes(1)
        # sleep(5)


def strobe(smart_plugs, interval=0.25):
    while True:
        turn_on_lights(smart_plugs)
        sleep(interval)
        turn_off_lights(smart_plugs)
        sleep(interval)


if __name__ == "__main__":
    smart_plugs = [SmartPlug(ip) for ip in config.light_plug_ips]

    # run(lights_on=True)
    # run()

    # turn_off_lights(smart_plugs)
    turn_on_lights(smart_plugs)
    # strobe(smart_plugs)
