import logging
from json import loads

from kafka import KafkaConsumer


logging.basicConfig(level=logging.INFO)

bootstrap_servers = ['localhost:9092']

try:
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest', group_id="1")
    consumer.subscribe(topics=['rawtweets'])
    logging.info("Kafka Consumer is connected and subscribed")
except Exception as e:
    logging.error(e)
    raise e
    
logging.info("Start Consuming")
for tweet in consumer:
    print(tweet.value.decode('utf-8'))
    consumer.commit()
    logging.info("Tweet Consumed")
