from kafka import KafkaConsumer
from json import loads
import logging

logging.basicConfig(level=logging.DEBUG)
bootstrap_servers = 'localhost:9092'
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest')
consumer.subscribe(topics=['rawtweets'])

for tweet in consumer:
    print(tweet.value.decode('utf-8'))