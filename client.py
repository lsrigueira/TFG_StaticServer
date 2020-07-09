import requests



url = "http://127.0.0.1:8000"
myobj = {'somekey': 'somevalue'}

if int(input("1)Get\n2)Post")) is 2:
    x = requests.post(url, data = myobj)
else:
    x = requests.get(url, data = myobj)
