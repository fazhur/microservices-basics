import requests

def post_to_facade(message: str):
    print(f'Posting message: {message}')
    response = requests.post('http://localhost:5000/api/v1.0/facade', json={'message': message})
    print(f'Response: {response.text}')
    return response.status_code

def get_from_facade():
    response = requests.get('http://localhost:5000/api/v1.0/facade')
    return response.text

messages = ['msg'+str(i) for i in range(1,11)]

for message in messages:
    print(post_to_facade(message))

for i in range(10):
    print(f'Iteration {i}')
    print(get_from_facade())
