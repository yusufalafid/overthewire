from paramiko import SSHClient

client = SSHClient()
client.load_system_host_keys()
# client.load_host_keys('/Users/YFS9048/.ssh/known_hosts')
# client.set_missing_host_key_policy(AutoAddPolicy())

client.connect('bandit.labs.overthewire.org', username='bandit0', password='bandit0', port=2220)
stdin, stdout, stderr = client.exec_command('cat readme')
print(stdout.read().decode("utf8"))

stdin.close()
stdout.close()
stderr.close()

client.close()