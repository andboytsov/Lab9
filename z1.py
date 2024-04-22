import requests

def get_students():
    response = requests.get('http://127.0.0.1:80/students')
    print(response.json())
    return(response.json())

get_students()
