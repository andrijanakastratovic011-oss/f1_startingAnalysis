import time
import json
import requests
from confluent_kafka import Producer

producer=Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")

while True:
    try:
        response=requests.get("https://api.openf1.org/v1/car_data?driver_number=1&speed>=350")
        if response.status_code==200:
            data=response.json()
            print("Podaci uspešno učitani!")
            for d in data:
                msg=json.dumps(d)
                producer.produce('f1_topic', value=msg, callback=delivery_report)
                producer.poll(0)
            producer.flush()

        elif response.status_code==429:
            print("Greška 429: API limit je prekoračen. Pokušaj ponovo kasnije sa manjim upitom.")
        
        elif response.status_code == 422:
            print("--- DETALJI GREŠKE 422 ---")
            try:
                print(response.json())  
            except:
                print(response.text)  
                print("--------------------------")
        
        else:
            print(f"Server je vratio kod: {response.status_code}")

    except Exception as e:
        print(f"Dogodila se greška pri povezivanju: {e}")

    time.sleep(10)