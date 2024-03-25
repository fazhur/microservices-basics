from flask import Flask, request
import hazelcast
import sys


app = Flask(__name__)

ip = '192.168.1.13'

@app.route('/api/v1.0/log', methods=['POST'])
def receive_uuid_message():
    print("received POST")
    facade_request = request.get_json()

    master_client = hazelcast.HazelcastClient(
        cluster_name="hazelcast-cluster-log",
        cluster_members = [f'{ip}:5701',
                           f'{ip}:5702',
                           f'{ip}:5703'])

    my_map = master_client.get_map("increment").blocking()
    my_map.put_if_absent(facade_request['UUID'], facade_request['msg'])
    master_client.shutdown()
    return 'Success', 200

@app.route('/api/v1.0/log', methods=['GET'])
def return_log():
    print("received GET")
    messages = ''
    master_client = hazelcast.HazelcastClient(
        cluster_name="hazelcast-cluster-log",
        cluster_members = [f'{ip}:5701',
                           f'{ip}:5702',
                           f'{ip}:5703'])

    my_map = master_client.get_map("increment").blocking()

    for key, value in my_map.entry_set():
        messages += value + '\n'
    return {'log': messages}, 200

if __name__ == '__main__':
    node_num = sys.argv[1]
    app.run(debug=False, port=6000 + int(node_num))
