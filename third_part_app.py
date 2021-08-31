import requests
import json
def get_function():
   res = requests.get(url='http://127.0.0.1:8000/api/')
   print(res.json())

get_function()
