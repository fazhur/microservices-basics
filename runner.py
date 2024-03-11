import requests

def post_to_facade(message: str):
    response = requests.post('http://localhost:5000/api/v1.0/facade', json={'message': message})
    return response.status_code

def get_from_facade():
    response = requests.get('http://localhost:5000/api/v1.0/facade')
    return response.text

messages = ['msg'+str(i) for i in range(1,11)]

for message in messages:
    print(post_to_facade(message))

print(get_from_facade())
