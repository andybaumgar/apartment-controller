from astral.sun import sun
from astral import LocationInfo
from datetime import date
from apartment_controller import config
from datetime import datetime
from time import sleep
import pytz

utc = pytz.UTC
eastern_tz = pytz.timezone("US/Eastern")


def eastern_day_seconds(input_datetime):
    eastern_time = input_datetime.astimezone(eastern_tz)
    midnight = eastern_time.replace(hour=0, minute=0, second=0, microsecond=0)
    return (eastern_time - midnight).seconds


def get_sunrise_sunset_seconds():
    location = LocationInfo(
        "New York",
        "USA",
        latitude=config.latitude,
        longitude=config.longitude,
        timezone=eastern_tz.zone,
    )
    LocationInfo()

    today = date.today()
    s = sun(location.observer, date=today)

    # get sunrise/sunset relative to eastern day
    sunrise_seconds = eastern_day_seconds(s["sunrise"])
    sunset_seconds = eastern_day_seconds(s["sunset"])

    return sunrise_seconds, sunset_seconds


def is_after_dusk():
    is_dark_out(sunset_offset=config.sunset_offset)


def is_dark_out(sunset_offset=0):
    sunrise, sunset = get_sunrise_sunset_seconds()
    current_time = eastern_day_seconds(datetime.now(utc))
    print(f"current_time: {current_time}")
    print(f"sunset + config.sunset_offset: {sunset + config.sunset_offset}")
    print(f"sunrise: {sunrise}")
    return current_time > sunset + config.sunset_offset * 3600 or current_time < sunrise


def is_asleep():
    current_time_hour = datetime.now(eastern_tz).hour
    print(f"current_time_hour: {current_time_hour}")
    print(f"config.bed_time_hour: {config.bed_time_hour}")
    print(f"config.wake_up_hour: {config.wake_up_hour}")
    return (
        current_time_hour >= config.bed_time_hour
        and current_time_hour < config.wake_up_hour
    )


def sleep_hours(seconds):
    sleep(seconds * 60 * 60)


def sleep_minutes(seconds):
    sleep(seconds * 60)


if __name__ == "__main__":
    # print(is_dark_out(sunset_offset=config.sunset_offset))
    print(is_asleep())
    # print(seconds_since_start_of_day(datetime.now()))
