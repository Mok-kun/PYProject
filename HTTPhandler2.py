#Created By Ashad Mouhamed
#HTTPhandler is a Python tool to send HTTP request and Data
#!/usr/bin/python


import os
import sys
import time
import socket
from colorama import Fore
from colorama import Style

#Local Varibale
reset = Style.RESET_ALL

def Main(host, port):
    sys.stdout.write(Fore.YELLOW+"\rWELCOME TO HTTPhandler PROGRAMME.\n"+reset)
    time.sleep(0.5)
    sys.stdout.write("\r[+]CREATING A SOCKET...\n")
    time.sleep(0.5)
    s = socket.socket()
    sys.stdout.write("\r[+]CONNECTING TO {0} AT PORT {1}\n".format(host, port))
    try:
        s.connect((host,int(port)))
    except socket.error as e:
        sys.stderr.write(Fore.RED+"[!]AN ERROR HAS OCCURRED WHILE CONNECTING TO {0}.:MYBE THE PORT IS CLOSED OR CHECK YOUR CONNECTION [AND TRY AGAIN]\n+reset".format(host))
        sys.stderr.write(Fore.RED+str(e)+'\n'+reset)
        sys.exit(1)
    sys.stdout.write("\r[+]CONNECTION HAS BEEN ESTABLISHED.\n")
    time.sleep(0.5)

    res = console()

    if res.lower() == 'change':
        host = raw_input(Fore.YELLOW+"ENTER THE NEW HOST ADDR: "+reset)
        port = raw_input(Fore.YELLOW+"ENTER THE NEW PORT NUM: "+reset)
        Main(host,port)
    if "GET" in res.upper():
        GET(res, s)
    if "HEAD" in res.upper():
        HEAD(res,s)
    else:
        sys.stdout.write("[+]SENDING DATA TO {0}..\n".format(host))
        time.sleep(0.5)
        s.sendall(str(res)+"\r\n\r\n")
        sys.stdout.write("[+]DATA HAS BEEN SENT CORRECTLY.\n")
        sys.stdout.write("[+]WAINTING FOR DATA.\n")
        mesa = s.recv(1024)
        sys.stdout.write(Fore.BLUE+mesa+reset+"\n")


    return 0


def GET(data,s):#if The data wanna be sent was a Get requeste
    sys.stdout.write("[+]SENDING DATA TO {0}..\n")
    time.sleep(0.5)
    s.sendall(str(data)+"\r\n\r\n")
    sys.stdout.write("[+]DATA HAS BEEN SENT CORRECTLY.\n")
    sys.stdout.write("[+]WAINTING FOR DATA.\n")
    if "html" in data or "GET / HTTP/1.1" in data:
        mesa = ""
        while "</html>" not in mesa:
            mesa += s.recv(1024)
    else:
        mesa = s.recv(2024)
    if mesa:
            sys.stdout.write("[+]DATA HAS BEEN DELIVERED..\n")
            os.system('clear')
            sys.stdout.write(Fore.BLUE+mesa+reset+"\n")
            chose = raw_input(Fore.YELLOW+"DO YOU WANNA SAVE THIS DATA:[YES][NO] "+reset)
            if chose.lower() == 'yes' or chose.lower() == 'y':
                FileSave(mesa)
            else:
                pass
            exit(0)
    else:
        sys.stderr.write(Fore.RED+"[!]TIMEOUT ERROR.\n"+reset)
        exit(1)

def HEAD(data,s):#IF the data wanna be sent was a head requeste
    sys.stdout.write("[+]SENDING DATA TO {0}..\n")
    time.sleep(0.5)
    s.sendall(str(data)+"\r\n\r\n")
    sys.stdout.write("[+]DATA HAS BEEN SENT CORRECTLY.\n")
    sys.stdout.write("[+]WAITING FOR DATA.\n")
    mesa = s.recv(1024)
    if mesa:
            sys.stdout.write("[+]DATA HAS BEEN DELIVERED..\n")
            os.system('clear')
            sys.stdout.write(Fore.BLUE+mesa+reset+"\n")
            chose = raw_input(Fore.YELLOW+"DO YOU WANNA SAVE THIS DATA:[YES][NO] "+reset)
            if chose.lower() == 'yes' or chose.lower() == 'y':
                FileSave(mesa)
            exit(0)
    else:
        sys.stderr.write(Fore.RED+"[!]TIMEOUT ERROR.\n"+reset)
        exit(1)

def FileSave(data):
    filename = str(raw_input("CHOSE THE FILENAME: "))
    with open(filename, 'a+') as file:
            for i in data:
                file.write(i)
            file.write('\n')
    time.sleep(1)
    sys.stdout.write('[+]THE FILE IS CREATED , THE DATA HAS BEEN SAVED\n')
    file.close()
    exit(0)
def console():
    res = raw_input(">>>> ")
    return res

def main():
    try:
        host = sys.argv[1]
        port = sys.argv[2]
    except:
        sys.stderr.write(Fore.RED+"[!]AN ERROR OCCURRED : YOU DIDN'T INCLUDE HOST AND PORT IN ARGUMENTS FIELD\n"+reset)
        host = raw_input(Fore.YELLOW+"ENTER THE HOST ADDR: "+reset)
        port = raw_input(Fore.YELLOW+"ENTER THE PORT NUM: "+reset)
    host = str(socket.gethostbyname(host))
    Main(host,port)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt :
        re = raw_input(Fore.RED+"\nDO YOU WANNA END THE PROGRAMME.[YES][NO]"+reset)
        if re.lower() == 'yes' or re.lower() == 'y':
            sys.stdout.write("GOODBYE\n")
            sys.exit(0)
        else:
            pass
