import json
from kafka.producer import KafkaProducer
from time import sleep
from datetime import datetime

BOOTSTRAP_SERVERS = ['localhost:9092']
TOPIC = 'kafkatest'

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                         value_serializer=lambda m: json.dumps(m).encode('ascii'))

while 1:
    producer.send(topic=TOPIC,
                  value="It's still working! " + str(datetime.now().time()))
    sleep(1)