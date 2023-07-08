import pika
import time

duration = 10 * 60  # Duration in seconds
interval = 15  # Interval in seconds

end_time = time.time() + duration

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


while time.time() < end_time:
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    time.sleep(interval)
connection.close()



