import subprocess
# defining ips in range of 192.168.1.1 to 1.10

filename=open("hosts1.txt","r")
f = open("hoststatus.txt","w")
def ping(host):

    #Using subprocess run
    ping_reply= subprocess.Popen(["ping","-c","3",host.rstrip()],stderr=subprocess.PIPE,stdout=f,text=True)
    print(ping_reply.returncode)
    print(ping_reply.communicate()[0])

for line in filename:
    ping(line)


