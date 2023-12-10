import json
import pymysql
import paho.mqtt.client as mqtt

broker_address = "127.0.0.1"
broker_port = 1883

db_host = 'localhost'
db_user = 'scott'
db_password = 'tiger'
db_name = 'mydb'

conn = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name, charset='utf8')
cursor = conn.cursor()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # 센서 데이터를 발행할 토픽 설정
    client.subscribe("sensor_data")


def save_to_database(temperature, brightness, humidity, timestamp):
    query = f"INSERT INTO sensor_data (temperature, brightness, humidity, timestamp) VALUES ({temperature}, {brightness}, {humidity}, '{timestamp}')"
    cursor.execute(query)
    conn.commit()

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8"))
    temperature = payload["temperature"]
    brightness = payload["brightness"]
    humidity = payload["humidity"]
    timestamp = payload["timestamp"]

    save_to_database(temperature, brightness, humidity, timestamp)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port)

client.loop_forever()
