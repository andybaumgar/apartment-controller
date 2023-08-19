from influxdb import InfluxDBClient

from apartment_controller import config


def get_current_temperature():
    client = InfluxDBClient(
        host="192.168.0.153", port=8086, password="admin", username="admin"
    )
    client.switch_database("apartment")

    query = f'SELECT * FROM "temperature" ORDER BY time DESC LIMIT 1'

    try:
        temperature = next(client.query(query).get_points())["value"]
        return temperature + config.temp_offset
    except:
        return None


if __name__ == "__main__":
    get_current_temperature()
