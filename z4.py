import requests

def delete_student(n):
    url = 'http://127.0.0.1:80/students/' + str(n)
    response = requests.delete(url)
    print(response.json())
    return(response.json())

n = int(input("Введите номер студента n: "))
delete_student(n)