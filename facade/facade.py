from flask import Flask, request
import requests
import uuid

app = Flask(__name__)


@app.route('/api/v1.0/facade', methods=['POST'])
def receive_message():
    client_request = request.get_json(force=True)
    message = client_request['message']
    uuid = generate_uuid(message)
    response = requests.post('http://localhost:5001/api/v1.0/log', json={'UUID': uuid, 'msg': message})
    return 'Success', 200

def generate_uuid(message):
    return str(uuid.uuid4())

@app.route('/api/v1.0/facade', methods=['GET'])
def respond_message():
    log = send_to_log()['log']
    msg = send_to_msg()['message']
    return log + msg, 200
    
def send_to_log():
    response = requests.get('http://localhost:5001/api/v1.0/log')
    return response.json()

def send_to_msg():
    response = requests.get('http://localhost:5003/api/v1.0/msg')
    return response.json()


if __name__ == '__main__':
    app.run(debug=False, port=5002)
