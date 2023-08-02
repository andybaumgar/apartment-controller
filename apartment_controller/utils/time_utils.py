from astral.sun import sun
from astral import LocationInfo
from datetime import date
from apartment_controller import config
from datetime import datetime
from time import sleep
import pytz

utc = pytz.UTC
eastern_tz = pytz.timezone("US/Eastern")


def get_sunrise_sunset():
    location = LocationInfo(latitude=config.latitude, longitude=config.longitude)
    LocationInfo()

    today = date.today()
    s = sun(location.observer, date=today)

    return s["sunrise"], s["sunset"]


def is_dark_out():
    sunrise, sunset = get_sunrise_sunset()
    current_time = datetime.now(utc)
    return current_time > sunset or current_time < sunrise


def is_asleep():
    current_time_hour = datetime.now(eastern_tz).hour
    return (
        current_time_hour >= config.bed_time_hour
        and current_time_hour < config.wake_up_hour
    )


def sleep_hours(seconds):
    sleep(seconds * 60 * 60)


def sleep_minutes(seconds):
    sleep(seconds * 60)
