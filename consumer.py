from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import logging


logging.basicConfig(level=logging.ERROR)
logging.info("meh")
bootstrap_servers = 'localhost:9092'
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest')
consumer.subscribe(topics=['rawtweets'])
logging.info('this shit was created')

for tweet in consumer:
    logging.info('whats wrong?T_T')
    print(tweet.value.decode('utf-8'))