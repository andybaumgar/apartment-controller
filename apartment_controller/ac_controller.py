import os
from enum import Enum
from time import sleep

from dotenv import load_dotenv
from kasa import SmartPlug

from apartment_controller import config
from apartment_controller.config import cycle_time_hours
from apartment_controller.utils.async_utils import async_to_sync
from apartment_controller.utils.temp_utils import get_current_temperature
from apartment_controller.utils.time_utils import is_asleep, sleep_hours

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


class Mode(Enum):
    RUN = 1
    SLEEP = 2


def get_target_temperature():
    if is_asleep():
        return config.sleep_target_temperature
    else:
        return config.waking_target_temperature


def needs_cooling(temperature):
    return temperature > (get_target_temperature() + 1)


def needs_heating(temperature):
    return temperature < (get_target_temperature() - 1)


def run():
    mode = Mode.RUN
    ran_hours = 0
    slept_hours = 0
    print("Running AC controller")
    ac_smart_plug = SmartPlug(config.ac_plug_ip)
    fan_smart_plug = SmartPlug(config.ac_fan_ip)
    smart_plugs = [ac_smart_plug, fan_smart_plug]
    turn_on_ac(smart_plugs)
    print("Connected to smart plug")

    while True:
        temperature = get_current_temperature()

        # check if AC should turn off
        if mode == Mode.RUN and (
            ran_hours >= config.ac_run_length_hours or needs_heating(temperature)
        ):
            mode = Mode.SLEEP
            ran_hours = 0
            turn_off_ac(smart_plugs)

        # check if AC should turn on
        if (
            mode == Mode.SLEEP
            and slept_hours >= config.ac_sleep_length_hours
            and needs_cooling(temperature)
        ):
            mode = Mode.RUN
            slept_hours = 0
            turn_on_ac(smart_plugs)

        # increment counts and sleep
        if mode == Mode.RUN:
            ran_hours += cycle_time_hours
        elif mode == Mode.SLEEP:
            slept_hours += cycle_time_hours

        sleep_hours(cycle_time_hours)


if __name__ == "__main__":
    # ac_smart_plug = SmartPlug(config.ac_plug_ip)
    # fan_smart_plug = SmartPlug(config.ac_fan_ip)
    # smart_plugs = [ac_smart_plug, fan_smart_plug]
    # # run()
    # turn_off_ac([ac_smart_plug, fan_smart_plug])
    # temperature = get_current_temperature()
    temperature = 74
    print(needs_cooling(temperature))
    print(needs_heating(temperature))
