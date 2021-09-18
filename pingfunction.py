import subprocess
# defining ips in range of 192.168.1.1 to 1.10
ips = ["192.168.0.{}".format(i) for i in range(1,11)]
def ping(host):
    #Using subprocess run
    ping_reply= subprocess.Popen(["ping","-c","1",host],stderr=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
    print(ping_reply.returncode)
    print(ping_reply.communicate()[0])

for ip in ips:
    print(ping(ip))

