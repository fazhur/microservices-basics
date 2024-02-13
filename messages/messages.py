from flask import Flask

app_msg = Flask(__name__)

@app_msg.route('/api/v1.0/msg', methods=['GET'])
def return_test_message():
    return {'message': 'Developing...'}, 200

if __name__ == '__main__':
    app_msg.run(debug=False, port=5003)
