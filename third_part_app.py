import requests
import json
def get_function(id = None):
   dt = json.dumps({'id':id})
   res = requests.get(url='http://127.0.0.1:8000/api/',data=dt)
   print(res.json())

#get_function()

def post_function(id = None):
   dt = json.dumps({'full_name':'Hari Khanal','address':'Jorpati','salary':36520})
   res = requests.post(url='http://127.0.0.1:8000/api/',data=dt)
   print(res.json())

post_function()
