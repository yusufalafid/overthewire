import requests

url="http://natas1.natas.labs.overthewire.org"
username="natas1"
password="g9D9cREhslqBKtcA2uocGHPfMZVzeFK6"

response = requests.get(url, auth=(username, password))
# print(response.text)
str="natas2"
for line in response.text.splitlines():
    if str in line:
        l=line.split()
        print(l[5])