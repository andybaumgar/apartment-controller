import asyncio
from kasa import SmartPlug
from dotenv import load_dotenv
import os
from ac_controller.async_utils import async_to_sync
from time import sleep

load_dotenv()


@async_to_sync
async def turn_off_ac(smart_plug):
    await smart_plug.turn_off()
    print("AC turned off")


if __name__ == "__main__":
    smart_plug = SmartPlug(os.environ.get("PLUG_IP"))
    turn_off_ac(smart_plug)
    # run()
