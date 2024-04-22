import requests


def get_student(n):
    url = 'http://127.0.0.1:80/students/' + str(n)
    response = requests.get(url)
    print(response.json())
    return response.json()

n = int(input("Введите номер студента n: "))
get_student(n)