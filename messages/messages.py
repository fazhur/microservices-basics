from flask import Flask
import hazelcast
import sys
import subprocess

app_msg = Flask(__name__)

ip = '192.168.1.13'

memory = []

@app_msg.route('/api/v1.0/msg', methods=['GET'])
def return_test_message():
    print(memory)
    return {'message': '\n'.join(memory)}, 200

class QueueListener:
    def __init__(self):
        print("Init started")
        self.client = hazelcast.HazelcastClient(
            cluster_name="hazelcast-cluster-log",
            cluster_members=[f'{ip}:5701', f'{ip}:5702', f'{ip}:5703']
        )

    def create_queue(self, num):
        self.queue = self.client.get_queue(f"{num}-msg").blocking()
        self.queue.add_listener(include_value=True, item_added_func=self.on_item_added)

    def on_item_added(self, event):
        print(f"Received {event.item}")
        memory.append(event.item)

if __name__ == '__main__':
    node_num = sys.argv[1]
    queue_listener = QueueListener()
    queue_listener.create_queue(node_num)
    app_msg.run(debug=False, port=6100 + int(node_num))
