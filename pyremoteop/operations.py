

def default(client):
    stdin, stdout, stderr = client.exec_command('cat /etc/fstab')
    for line in stdout:
        print('... ' + line.strip('\n'))
