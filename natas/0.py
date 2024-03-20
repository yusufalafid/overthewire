import requests

url="http://natas0.natas.labs.overthewire.org"
username="natas0"
password="natas0"

response = requests.get(url, auth=(username, password))
str="natas1"
for line in response.text.splitlines():
    if str in line:
        l=line.split()
        print(l[5])
        with open('password.txt', 'w') as f:
            f.write(l[5])