import requests

def post_to_facade(message: str):
    print(f'Posting message: {message}')
    response = requests.post('http://127.0.0.1:5000/api/v1.0/facade', json={'message': message})
    print(f'Response: {response.text}')
    return response.status_code

def get_from_facade():
    response = requests.get('http://127.0.0.1:5000/api/v1.0/facade')
    return response.json()['result']

messages = ['msg'+str(i) for i in range(1,11)]

for message in messages:
    print(post_to_facade(message))

print(get_from_facade())
