from django.test import TestCase
import requests

import requests

url = "http://127.0.0.1:8000/api/auth"

#5. 왜 request.get은 안 될까?
response = requests.post(url, data={'username':'test2', 'password':'test2'})

print(response.text)
myToken = response.text

header = {'Authorization':'Token f81d8e32d20768ede1b6b6d45998b3f2671bd161'}
response = requests.get('http://127.0.0.1:8000/api/student_list', headers=header)
print(response.text)