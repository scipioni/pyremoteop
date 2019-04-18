import argparse
import paramiko
import warnings

warnings.filterwarnings(action='ignore',module='.*paramiko.*')

from pyremoteop import operations


ap = argparse.ArgumentParser()
ap.add_argument('ip', nargs='+', help="list of devices")
#ap.add_argument('--ocr', action='store_true', default=False)
ap.add_argument('--credentials', default='root:xyz,admin:admin')
ap.add_argument('--operations', default='default')

args = ap.parse_args()

def opdevice(ip):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for credential in args.credentials.split(','):
        print("connecting '%s' with credential %s" % (ip, credential))
        username, password = credential.split(':')
        try:
            client.connect(ip, username=username, password=password)
            break
        except paramiko.ssh_exception.AuthenticationException:
            pass
    for operation_name in args.operations.split(','):
        operation = getattr(operations, operation_name)
        operation(client)
    client.close()


def main():
    for ip in args.ip:
        opdevice(ip)
