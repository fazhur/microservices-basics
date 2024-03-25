from flask import Flask, request
import hazelcast
import requests
import uuid
import random
import subprocess

app = Flask(__name__)

# ip = '192.168.1.13'
ip = '172.20.96.1'

messages_nodes = 2
log_nodes = 3

def select_log_node():
    return f'http://localhost:600{random.randint(1,log_nodes)}/api/v1.0/log'
    # return f'http://localhost:6002/api/v1.0/log'

def select_msg_node():
    return f'http://localhost:610{random.randint(1,messages_nodes)}/api/v1.0/msg'
    # return f'http://localhost:6101/api/v1.0/msg'

def put_message(message):
    print("Trying to access queue")
    client = hazelcast.HazelcastClient(
        cluster_name="hazelcast-msg-cluster")
    msg_queue = client.get_queue("msg").blocking()
    print('Queue received')
    msg_queue.put(message)
    print("puted in queue")
    return 'Success', 200

@app.route('/api/v1.0/facade', methods=['POST'])
def receive_message():
    print("received POST")
    client_request = request.get_json(force=True)
    message = client_request['message']
    print(f'Message: {message}')
    # uuid = generate_uuid(message)
    result = put_message(message)
    # response = requests.post(select_log_node(), json={'UUID': uuid, 'msg': message})
    return result

def generate_uuid(message):
    return str(uuid.uuid4())

@app.route('/api/v1.0/facade', methods=['GET'])
def respond_message():
    # log = send_to_log()['log']
    log = 'test \n'
    msg = send_to_msg()['message']
    return log + msg, 200

def send_to_log():
    response = requests.get(select_log_node())
    return response.json()

def send_to_msg():
    response = requests.get(select_msg_node())
    return response.json()

print('Facade running5')
if __name__ == '__main__':
    print('Facade running')
    try:
        node_name = f"hazelcast-msg-node-master"
        command = [
            "docker", "run", "-it", "--name", node_name, "--rm",
            "-e", f"HZ_NETWORK_PUBLICADDRESS={ip}:5710",
            "-e", "HZ_CLUSTERNAME=hazelcast-msg-cluster",
            "-p", f"5710:5710",
            "hazelcast/hazelcast:5.3.6"
        ]
        subprocess.Popen(command)
        app.run(debug=False, port=5000)
    finally:
        subprocess.Popen(["docker", "stop", node_name])