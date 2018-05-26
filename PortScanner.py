#Most used Port scanner Created by Ashad Mouhamed
#Have fun using it
import socket
import time
import os
import sys
from colorama import Fore
from colorama import Style

##################
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW
reset = Style.RESET_ALL
######################

def Main(host):
    sys.stdout.write(Fore.YELLOW+"\rWELCOME TO PortScanner PROGRAMME.\n"+reset)
    time.sleep(0.5)
    sys.stdout.write("\r[+]CREATING A SOCKET...\n")
    time.sleep(0.5)
    #s = socket.socket()
    r = {"ftp":21,"ssh":22,"Telnet":23,"http":80,"smtp":25,"dns":53,"dhcp":67,"tftp":68,"pop":110,"ntp":123,"imap":143,"snmp":161,"bgp":179,"ldap":389,"https":443,"ldaps":636}
    report = "PortScanner report for {0}:\nPORT\t\tSTATE\t\tSERVICE\n".format(host)
    for i in r.keys():
        s = socket.socket()
        if s.connect_ex((host,r[i])) == 0:
            sys.stdout.write(blue+"[+]PORT {0} IS OPEN.\n".format(r[i])+reset)
            s.close()
            report +="{0}\t\topen\t\t{1}\n".format(r[i],i.upper())
            time.sleep(0.5)

        else:
            sys.stdout.write(blue+"[+]PORT {0} IS CLOSE.\n".format(r[i])+reset)
            report +="{0}\t\tclose\t\t{1}\n".format(r[i],i.upper())
            time.sleep(0.5)
            s.close()
    os.system("clear")
    sys.stdout.write(yellow+report+reset)

def main():
    try:
        host = sys.argv[1]
    except:
        sys.stderr.write(Fore.RED+"[!]AN ERROR OCCURRED : YOU DIDN'T INCLUDE HOST ADDR IN ARGUMENTS FIELD\n"+reset)
        host = raw_input(Fore.YELLOW+"ENTER THE HOST ADDR: "+reset)
    host = str(socket.gethostbyname(host))
    Main(host)

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
