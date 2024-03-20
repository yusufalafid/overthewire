import requests, re, base64
from bs4 import BeautifulSoup

url="http://natas8.natas.labs.overthewire.org/"
username="natas8"
# read password from generated file
file=open('password.txt', 'r')
password=file.read()

# req=requests.get(url, auth=(username, password))
# print(req.text)
source="index-source.html"
src=requests.get(url+source, auth=(username, password)).text

# Parse the encodedsecret
soup = BeautifulSoup(src, 'html.parser')
element=soup.find('span').text.strip()
encodedsecret=re.search(r'"([0-9a-f]+)"', element).group(1)
# print(secret)

# Decode the secret
secret=base64.b64decode(bytes.fromhex(encodedsecret)[::-1]).decode('utf-8')
# print(bytes)

#send decoded secret
data={
    'secret': secret,
    'submit': 'Submit+Query'
}
solve=requests.post(url, data=data, auth=(username, password))
# print(solve.text)

# parse password
str='natas9'
for line in solve.text.splitlines():
    if str in line:
        l=line.split()
        # print(l[7])
        with open('password.txt', 'w') as f:
            f.write(l[7])
file.close()