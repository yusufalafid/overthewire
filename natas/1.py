import requests

url="http://natas1.natas.labs.overthewire.org"
username="natas1"
file=open('password.txt', 'r')
password=file.read()

response = requests.get(url, auth=(username, password))

str="natas2"
for line in response.text.splitlines():
    if str in line:
        l=line.split()
        print(l[5])
        with open('password.txt', 'w') as f:
            f.write(l[5])
file.close()