import requests

def update_student(n, updated_student_data):
    url = 'http://127.0.0.1:80/students/' + str(n)
    response = requests.put(url, json=updated_student_data)
    print(response.json())
    return(response.json())

n = int(input("Введите номер студента n: "))
updated_student_data = {"name": "Новый Студент", "age": 23, "major": "Химия"}

update_student(n, updated_student_data)