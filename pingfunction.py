import subprocess
# defining ips in range of 192.168.1.1 to 1.10
ips = ["192.168.1.{}".format(i) for i in range(1,11)]
def ping(host):
    #Using subprocess run
    ping_reply= subprocess.run(["ping","-c","1",host],stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    result = ""
    if ping_reply.returncode==0:
        # For Unreachable case returncode is also 0 , hence no response from host added
        if "unreachable" in str(ping_reply.stdout):
            result= ("\n* No response from host %s"% host)
        else:
            result= ("\n* %s is Reachable"% host)
    elif ping_reply.returncode!=0:
        result= ("\n %s is not Reachable"% host)
    return result
for ip in ips:
    print(ping(ip))

