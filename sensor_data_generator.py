import random
import time
import json
from datetime import datetime
import paho.mqtt.publish as publish

broker_address = "127.0.0.1"
broker_port = 1883

def generate_sensor_data():
    temperature = random.uniform(10, 30)
    brightness = random.uniform(0, 100)
    humidity = random.uniform(20, 80)
    current_time = datetime.now().isoformat()
    
    return temperature, brightness, humidity, current_time

def print_sensor_data(temperature, brightness, humidity, current_time):
    print(f"Temperature: {temperature:.2f} °C, Brightness: {brightness:.2f} lux, Humidity: {humidity:.2f}%, Current Time: {current_time}\n")

while True:
    temperature, brightness, humidity, current_time = generate_sensor_data()

    sensor_data = {
        "temperature": temperature,
        "brightness": brightness,
        "humidity": humidity,
        "timestamp": current_time
    }
    
    publish.single("sensor_data", json.dumps(sensor_data), hostname=broker_address, port=broker_port)

    print_sensor_data(temperature, brightness, humidity, current_time)
    time.sleep(5)