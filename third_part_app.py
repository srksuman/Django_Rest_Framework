import requests
import json
def get_function(id = None):
   dt = json.dumps({'id':id})
   res = requests.get(url='http://127.0.0.1:8000/api/',data=dt)
   print(res.json())

# get_function()

def post_function(id = None):
   dt = json.dumps({'full_name':'Hari Khanal','address':'Jorpati','salary':36520})
   res = requests.post(url='http://127.0.0.1:8000/api/',data=dt)
   print(res.json())

# post_function()

def put_function():
   dt = json.dumps({'id':2,'full_name':'Sujan Raj','salary':2000,'address':'Thali'})
   res = requests.put(url='http://127.0.0.1:8000/api/',data=dt)
   print(res.json())

# put_function()

def delete_function():
   dt = json.dumps({'id':2})
   res = requests.delete(url='http://127.0.0.1:8000/api/',data=dt)
   print(res.json())

delete_function()