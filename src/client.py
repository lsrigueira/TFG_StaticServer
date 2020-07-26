import requests
from basededatos import mybd
from requests import get
url = "http://192.168.8.103:8000"
myobj = {'somekey': 'somevalue'}

prueba = mybd()
if int(input("1)Get\n2)Post")) is 2:
    #prueba.insertIp("MAC","IPPRIVADA","IPPUBLICA")
    ip = get('https://api.ipify.org').text
    print('My public IP address is:', ip)
    #x = requests.post(url, data = myobj)
else:
    x = requests.get(url, data = myobj)
