import requests

url="http://natas0.natas.labs.overthewire.org"
username="natas0"
password="natas0"

response = requests.get(url, auth=(username, password))
pass = response.
print(response.text)