import pika, json

params = pika.URLParameters('amqps://vzqbgtbb:kJyeCvI7IDTzcbowv2_P_tZ7X5-a6g5N@rattlesnake.rmq.cloudamqp.com/vzqbgtbb')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
