# import AMQP
import pika, os
import json

#koneksi AMQP
url = os.environ.get('CLOUDAMQP_URL','amqps://bqnpmbjb:lnpCxdFf-q7KsTZF0nkI5RKUkMxlaCTb@chimpanzee.rmq.cloudamqp.com/bqnpmbjb')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel
channel.queue_declare(queue='Testing')  # Declare a queue

amqppayload = json.dumps({'volt': "1", 'ampere': "5", 'kwh': "9999"})

channel.basic_publish(exchange='',routing_key='Testing',body=amqppayload)