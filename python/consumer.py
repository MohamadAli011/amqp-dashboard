import pika, os
import websocket
import time
import json
from websocket import create_connection

# WEBSOCKET
# websocket.enableTrace(True)
ws = create_connection('ws://localhost:3030/')

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://bqnpmbjb:lnpCxdFf-q7KsTZF0nkI5RKUkMxlaCTb@chimpanzee.rmq.cloudamqp.com/bqnpmbjb')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='Testing') # Declare a queue

def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))
  print(" [v] Send to websocket server ")
  # websocket payload 
  payload = json.loads(body) #convert to json
  ws.send(json.dumps(payload)) #send to websocket server with json payload
  print(" [v] Payload sent to websocket server")

channel.basic_consume('Testing', callback, auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()