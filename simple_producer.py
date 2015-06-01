from kafka import SimpleProducer,KafkaClient
import time 

class KafkaProducer:

	def __init__(self):
		kafkahandle = KafkaClient("localhost:9092")
		self.producer = SimpleProducer(kafkahandle)

	def kafka_producer(self,topicname='harish_t',message=time.time()):
		_msg=str(message)   #Converting to string explicitly since kafka expects string 
		self.producer.send_messages(topicname,_msg)


KafkaObj=KafkaProducer()
KafkaObj.kafka_producer()

