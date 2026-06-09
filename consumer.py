from confluent_kafka import Consumer
from sqlalchemy import create_engine, text
import os
import json

engine=create_engine("postgresql://postgres:12345678@172.29.144.1:5432/f1_database")
with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS car_data (
            id SERIAL PRIMARY KEY,
            brake INTEGER,
            date TIMESTAMP,
            driver_number INTEGER,
            drs INTEGER,
            meeting_key INTEGER,
            n_gear INTEGER,
            rpm INTEGER,
            session_key INTEGER,
            speed INTEGER,
            throttle INTEGER
        );
    """))

conf={'bootstrap.servers': 'localhost:9092', 'group.id': 'my-group', 'auto.offset.reset': 'earliest', 'enable.auto.commit': True, 'auto.commit.interval.ms': 1000}
consumer=Consumer(conf)
consumer.subscribe(['f1_topic'])
try:
    while True:
        msg=consumer.poll(1.0)
        if msg is None:
             continue
        if msg.error():
             print(f"Greska na Kafki: {msg.error()}")
             continue
        message = msg.value().decode('utf-8') if msg.value() else '{}'
        print(f"--- NOVA PORUKA SA KAFKE (Offset: {msg.offset()}) ---")
        print(message)
        data = json.loads(message)
        records = data if isinstance(data, list) else [data]
        with engine.begin() as conn:
            car_data=text('INSERT INTO car_data (brake, date, driver_number, drs, meeting_key, n_gear, rpm, session_key, speed, throttle) VALUES (:brake, :date, :driver_number, :drs, :meeting_key, :n_gear, :rpm, :session_key, :speed, :throttle)')
            for row in records:
                conn.execute(car_data, {
                        "brake": row.get("brake"),
                        "date": row.get("date"),
                        "driver_number": row.get("driver_number"), 
                        "drs": row.get("drs"), 
                        "meeting_key": row.get("meeting_key"), 
                        "n_gear": row.get("n_gear"), 
                        "rpm": row.get("rpm"), 
                        "session_key": row.get("session_key"), 
                        "speed": row.get("speed"), 
                        "throttle": row.get("throttle")
                })
except KeyboardInterrupt:
    pass
finally:
    consumer.close()