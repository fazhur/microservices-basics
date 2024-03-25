from flask import Flask, request
import hazelcast
import requests
import uuid
import random
import subprocess

app = Flask(__name__)

ip = '192.168.1.13'

messages_nodes = 2
log_nodes = 3

def select_log_node():
    return f'http://localhost:600{random.randint(1,log_nodes)}/api/v1.0/log'
    # return f'http://localhost:6002/api/v1.0/log'


def put_message(message):
    print("Trying to access queue")
    writer = random.choice(queue_writers)
    writer.write(message)
    print("puted in queue")
    return 'Success', 200

@app.route('/api/v1.0/facade', methods=['POST'])
def receive_message():
    print("received POST")
    client_request = request.get_json(force=True)
    message = client_request['message']
    print(f'Message: {message}')
    uuid = generate_uuid(message)
    result = put_message(message)
    response = requests.post(select_log_node(), json={'UUID': uuid, 'msg': message})
    return result

def generate_uuid(message):
    return str(uuid.uuid4())

@app.route('/api/v1.0/facade', methods=['GET'])
def respond_message():
    print("received GET")
    log = requests.get(select_log_node())
    print(log)
    log = log.json()['log']
    msg = ''
    for i in range(1, 3):
        responce = requests.get(f'http://localhost:610{i}/api/v1.0/msg')
        msg += responce.json()['message']
    return {'result': log + '\n' + msg}, 200

def send_to_log():
    response = requests.get(select_log_node())
    return response.json()


class QueueWriter:
    def __init__(self, num):
        print("Init started")
        self.client = hazelcast.HazelcastClient(
            cluster_name="hazelcast-cluster-log",
            cluster_members=[f'{ip}:5701', f'{ip}:5702', f'{ip}:5703']
        )
        self.queue = self.client.get_queue(f"{num}-msg").blocking()
        self.id = num

    def write(self, message):
        self.queue.put(message)


if __name__ == '__main__':
    print('Facade running')
    queue_writers = [QueueWriter(i) for i in range(1, 3)]
    app.run(debug=False, port=5000)