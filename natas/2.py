import requests

url="http://natas2.natas.labs.overthewire.org/files/users.txt"
username="natas2"
password="h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7"

response = requests.get(url, auth=(username, password))
# print(response.text)
str="natas3"
for line in response.text.splitlines():
    if str in line:
        l=line.split(":")
        print(l[1])