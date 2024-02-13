from flask import Flask, request

app = Flask(__name__)

hash_log = {}

@app.route('/api/v1.0/log', methods=['POST'])
def receive_uuid_message():
    facade_request = request.get_json()
    hash_log[facade_request['UUID']] = facade_request['msg']
    return 'Success', 200

@app.route('/api/v1.0/log', methods=['GET'])
def return_log():
    messages = ''
    for key, value in hash_log.items():
        messages += value + '\n'
    return {'log': messages}, 200

if __name__ == '__main__':
    app.run(debug=False, port=5001)
