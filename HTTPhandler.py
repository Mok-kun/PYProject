#Created By Ashad Mouhamed
#HTTPhandler is a Python tool to send HTTP request and Data 
#!/usr/bin/python


import os
import sys
import time
import socket


def Main(host, port):
    sys.stdout.write("\rWELCOME TO HTTPhandler PROGRAMME.\n")
    time.sleep(0.5)
    sys.stdout.write("\r[+]CREATING A SOCKET...\n")
    time.sleep(0.5)
    s = socket.socket()
    sys.stdout.write("\r[+]CONNECTING TO {0} AT PORT {1}\n".format(host, port))
    try:
        s.connect((host,int(port)))
    except socket.error as e:
        sys.stderr.write("[!]AN ERROR HAS ACCOURED WHILE CONNECTING TO {0}.:MYBE THE PORT IS CLOSED OR CHECK YOUR CONNECTION [AND TRY AGAIN]\n".format(host))
        sys.sterr.write(str(e)+'\n')
        sys.exit(1)
    sys.stdout.write("\r[+]CONNECTION HAS BEEN ESTABLESHED.\n")
    time.sleep(0.5)
    while True:
        res = console()
        if res.lower() == 'q':
            sys.stdout.write('[+]CLOSING CONNECTION...\n')
            time.sleep(1)
	    s.close()
            sys.stdout.write("[+]CONNECTION TO {0} CLOSED.\n".format(host))
            break
        if res.lower() == 'change':
            host = raw_input("ENTER THE NEW HOST ADDR: ")
            port = raw_input("ENTER THE NEW PORT NUM: ")
            Main(host,port)
        else:
            sys.stdout.write("[+]SENDING DATA TO {0}..\n")
            time.sleep(0.5)
            s.sendall(str(res)+"\r\n\r\n")
            sys.stdout.write("[+]DATA HAS BEEN SENT CORRECTLY.\n")
            sys.stdout.write("[+]WAINTING FOR DATA.\n")
            mesa = ""
	    mesa += s.recv(1024)
	    while "</html>" not in mesa:

		mesa += s.recv(1024)
	    if mesa:
                sys.stdout.write("[+]DATA HAS BEEN DELIEVERED..\n")
                os.system('clear')
                sys.stdout.write(mesa+"\n")
                chose = raw_input("DO YOU WANNA SAVE THIS DATA:[YES][NO] ")
                if chose.lower() == 'yes' or chose.lower() == 'y':
                    filename = str(raw_input("CHOSE THE FILENAME: "))
                    with open(filename, 'a+') as file:
                            for i in mesa:
                                file.write(i)
                            file.write('\n')
			    time.sleep(1)
			    sys.stdout.write('[+]THE FILE IS CREATED , THE DATA HAS BEEN SAVED\n')
                            file.close()
                else:
                    pass

def console():
    res = raw_input(">>>> ")
    return res

def main():
    try:
        host = sys.argv[1]
        port = sys.argv[2]
    except:
        sys.stderr.write("[!]AN ERROR : YOU DIDN'T INCLUDE HOST AND PORT IN ARGUMENTS FIELD\n")
        host = raw_input("ENTER THE HOST ADDR: ")
        port = raw_input("ENTER THE PORT NUM: ")
    host = str(socket.gethostbyname(host))
    Main(host,port)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt :
        re = raw_input("\nDO YOU WANNA END THE PROGRAMME.[YES][NO]")
        if re.lower() == 'yes' or re.lower() == 'y':
            sys.stdout.write("GOODBYE\n")
            sys.exit(0)
        else:
            main()

