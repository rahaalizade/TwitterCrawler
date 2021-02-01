from json import dumps
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
with open("rawtweets.txt", "r") as file:
    rawtweets = json.loads("{}".format(file.read()))
    for tweet in rawtweets:
        producer.send('rawtweets', (json.dumps(tweet)).encode('utf-8'))

producer.flush()