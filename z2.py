import requests

def post_student(student_data):
    response = requests.post('http://127.0.0.1:80/students',json=student_data)
    print(response.json())
    return response.json()

student_data = {"id": 4, "name": "Новый Студент", "age": 22, "major": "Биология"}
post_student(student_data)
