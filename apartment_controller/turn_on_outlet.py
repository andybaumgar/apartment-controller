from kasa import SmartPlug
from dotenv import load_dotenv
import os
from apartment_controller.utils.async_utils import async_to_sync

load_dotenv()


@async_to_sync
async def turn_off_plug(smart_plug):
    await smart_plug.turn_off()
    print("plug turned off")


if __name__ == "__main__":
    smart_plug = SmartPlug("192.168.0.136")
    turn_off_plug(smart_plug)
    # run()
