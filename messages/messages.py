# from flask import Flask, request
# import hazelcast
# import sys
# import subprocess

# app_msg = Flask(__name__)

# ip = '192.168.1.13'

# memory = []

# @app_msg.route('/api/v1.0/msg', methods=['GET'])
# def return_test_message():
#     return {'message': '\n'.join(memory)}, 200

# def save_message():
#     client = hazelcast.HazelcastClient(
#                 cluster_name="hazelcast-msg-cluster",
#                 cluster_members=[f'{ip}:5710',
#                                 f'{ip}:5711',
#                                 f'{ip}:5712'])
#     queue = client.get_queue("msg").blocking()
#     while True:
#         elem = queue.poll()
#         if not (elem is None):
#             memory.append(elem)
    

# if __name__ == '__main__':
#     try:
#         node_num = sys.argv[1]
#         node_name = f"hazelcast-msg-node-{node_num}"
#         command = [
#             "docker", "run", "-it", "--name", node_name, "--rm",
#             "-e", f"HZ_NETWORK_PUBLICADDRESS={ip}:571{node_num}",
#             "-e", "HZ_CLUSTERNAME=hazelcast-msg-cluster",
#             "-p", f"571{node_num}:5710",
#             "hazelcast/hazelcast:5.3.6"
#         ]
#         subprocess.Popen(command)
#         app_msg.run(debug=False, port=6100 + int(node_num))
#     finally:
#         subprocess.Popen(["docker", "stop", node_name])

from flask import Flask
import hazelcast
import sys
import subprocess

app_msg = Flask(__name__)

# ip = '192.168.1.13'
ip = '172.20.96.1'

memory = []

@app_msg.route('/api/v1.0/msg', methods=['GET'])
def return_test_message():
    return {'message': '\n'.join(memory)}, 200

class QueueListener:
    def __init__(self):
        print("Init started")
        self.client = hazelcast.HazelcastClient(
            cluster_name="hazelcast-msg-cluster"
            # cluster_members=[f'{ip}:5710', f'{ip}:5711', f'{ip}:5712']
        )
        self.queue = self.client.get_queue("msg").blocking()
        self.queue.add_item_listener(include_value=True, item_added_listener=self.on_item_added)

    def on_item_added(self, event):
        print(f"Received {event.item}")
        memory.append(event.item)

if __name__ == '__main__':
    try:
        node_num = sys.argv[1]
        node_name = f"hazelcast-msg-node-{node_num}"
        command = [
            "docker", "run", "-it", "--name", node_name, "--rm",
            "-e", f"HZ_NETWORK_PUBLICADDRESS={ip}:571{node_num}",
            "-e", "HZ_CLUSTERNAME=hazelcast-msg-cluster",
            "-p", f"571{node_num}:5710",
            "hazelcast/hazelcast:5.3.6"
        ]
        subprocess.Popen(command)
        queue_listener = QueueListener()
        app_msg.run(debug=False, port=6100 + int(node_num))
    finally:
        subprocess.Popen(["docker", "stop", node_name])
