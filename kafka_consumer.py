from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer

class Consumer(object):
        def __init__(self):
                self.__client = KafkaClient("localhost:9092")
                self.__consumer = SimpleConsumer(self.__client, "test-group", "sq")

        def consume(self):
             for message in self.__consumer:
                print(message.topic)

if __name__ == "__main__":
    c = Consumer()
    c.consume()
