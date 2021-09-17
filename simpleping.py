
#Program for pinging the hosts from file hosts1.txt
import subprocess
filename = open('hosts1.txt','r')
lines = filename.readlines()
for line in lines:
    response = subprocess.Popen(["ping","-c","1",line.rstrip()],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout,stderr = response.communicate()
#print(stdout)
#print(stderr)
    if (response.returncode==0):
        status = print(line.rstrip() + " is reachable")
    else:
        status = print(line.rstrip() + " is not reachable")
