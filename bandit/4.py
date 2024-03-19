
from paramiko import SSHClient

def is_human_readable(data):
    try:
        data.decode("utf8")
        return True
    except UnicodeDecodeError:
        return False

client = SSHClient()
client.load_system_host_keys()
client.connect('bandit.labs.overthewire.org', username='bandit4', password='2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe', port=2220)
x = range(10)
for i in x:
    filename= f"inhere/-file0{i}"
    stdin, stdout, stderr = client.exec_command(f"cat < {filename}")
    output = stdout.read()

    if is_human_readable(output):
        print(output.decode("utf8"))

stdin.close()
stdout.close()
stderr.close()

client.close()