from astral.sun import sun
from astral import LocationInfo
from datetime import date
from apartment_controller import config
from datetime import datetime
from time import sleep
import pytz

utc = pytz.UTC
local_tz = pytz.timezone(config.local_tz_name)


def get_seconds_since_midnight(input_datetime, tz):
    local_time = input_datetime.astimezone(tz)
    midnight = local_time.replace(hour=0, minute=0, second=0, microsecond=0)
    return (local_time - midnight).seconds


def get_sunrise_sunset_seconds_since_midnight(tz):
    location = LocationInfo(
        latitude=config.latitude,
        longitude=config.longitude,
        timezone=tz.zone,
    )
    LocationInfo()

    today = date.today()
    s = sun(location.observer, date=today)

    # get sunrise/sunset relative to eastern day
    sunrise_seconds = get_seconds_since_midnight(s["sunrise"], local_tz)
    sunset_seconds = get_seconds_since_midnight(s["sunset"], local_tz)

    return sunrise_seconds, sunset_seconds


def is_after_dusk():
    return is_dark_out(sunset_offset=config.sunset_offset)


def is_dark_out(sunset_offset=0):
    sunrise, sunset = get_sunrise_sunset_seconds_since_midnight(local_tz)
    current_time = get_seconds_since_midnight(datetime.now(utc), local_tz)
    print(f"current_time: {current_time}")
    print(f"sunrise: {sunrise}")
    return current_time > sunset + sunset_offset * 3600 or current_time < sunrise


def andy_is_asleep():
    current_time_hour = datetime.now(local_tz).hour
    print(f"current_time_hour: {current_time_hour}")
    print(f"config.bed_time_hour: {config.bed_time_hour}")
    print(f"config.wake_up_hour: {config.wake_up_hour}")
    return (
        current_time_hour >= config.bed_time_hour
        and current_time_hour < config.wake_up_hour
    )


def should_lights_dim():
    current_time_hour = datetime.now(local_tz).hour
    return current_time_hour >= config.should_lights_dim_hour


def sleep_hours(seconds):
    sleep(seconds * 60 * 60)


def sleep_minutes(seconds):
    sleep(seconds * 60)


if __name__ == "__main__":
    # print(is_dark_out(sunset_offset=config.sunset_offset))
    print(andy_is_asleep())
    # print(seconds_since_start_of_day(datetime.now()))
