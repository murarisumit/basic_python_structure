import json
import definations

#TODO
# 1.Add logging to it


def some_method(input_param):
    pass


def send_to_kafka(kafka_addr,kafka_topic, filtered_data):
    from kafka import KafkaProducer
    producer = KafkaProducer(bootstrap_servers=kafka_addr)
    producer.send(kafka_topic,bytes(filtered_data,'utf-8'))
    producer.flush()


if __name__ == "__main__":
    config = settings.config
    ENV = settings.ENV
    BROKERS_LIST = json.loads(settings.get(ENV, 'brokers_list'))

    # Debug flag
    DEBUG = config.get(ENV, 'debug')
    KAFKA_TOPIC = config.get(ENV, 'kafka_topic')

    send_to_kafka(BROKERS_LIST,KAFKA_TOPIC, fetch_data(inpt))
