import sqlite3


def save_data(data):
    conn = sqlite3.connect("weather_data.db")
    cur = conn.cursor()

    query1 = f"""
CREATE TABLE IF NOT EXISTS {data['name']}
(date,temperature,humidity,wind_speed);"""
    cur.execute(query1)

    query2 = f"""
INSERT INTO {data['name']}
VALUES {(data['date'], data['temp'], data['humidity'], data['wind_speed'])};"""

    cur.execute(query2)

    conn.commit()
    conn.close()

    print("New record saved in DB")


def display_data(table):
    conn = sqlite3.connect("weather_data.db")
    cur = conn.cursor()
    command = f"SELECT * FROM {table};"
    cur.execute(command)
    records = cur.fetchall()
    for i in records:
        print(i)
