import pymysql
import datetime
import random

db_host = 'localhost'
db_user = 'scott'
db_password = 'tiger'
db_name = 'mydb'

conn = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name, charset='utf8')
cursor = conn.cursor()

# 그래프 초기화 해주기

def get_realtime_data():
    query = "SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 100"
    cursor.execute(query)
    results = cursor.fetchall()
    return results

# 그래프 실시간 업데이트 해주기

# 애메이션 실행하기

# 데이터 베이스 연결종료

# 그프 랜더링