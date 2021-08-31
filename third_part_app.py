import requests
import json
def get_function(id = None):
   dt = json.dumps({'id':id})
   dt = json.dumps({'id':id})
   res = requests.get(url='http://127.0.0.1:8000/api/',data=dt)
   print(res.json())

get_function()
