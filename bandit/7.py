
from paramiko import SSHClient

def is_human_readable(data):
    try:
        data.decode("utf8")
        return True
    except UnicodeDecodeError:
        return False

client = SSHClient()
client.load_system_host_keys()
client.connect('bandit.labs.overthewire.org', username='bandit7', password='z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S', port=2220)
stdin, stdout, stderr = client.exec_command('')
# print(stdout.read().decode("utf8"))

x = stdout.read().decode("utf8") #.replace(" ", "\ ").splitlines
x = x.replace(" ", "\ ")
x = x.splitlines()
# print(repr(x))
for i in x:
    # filename= f"inhere/-file0{i}"
    # print(f"cat < {i}")
    stdin, stdout, stderr = client.exec_command(f"cat {i}")
    output = stdout.read()
    if is_human_readable(output):
        print(output.decode("utf8"))

stdin.close()
stdout.close()
stderr.close()

client.close()