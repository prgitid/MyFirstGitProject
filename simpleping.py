
#Program for pinging the hosts from file hosts1.txt
import subprocess
filename = open('hosts1.txt','r')
f = open('hoststatus.txt','w')
lines = filename.readlines()
for line in lines:
    response = subprocess.Popen(["ping","-c","1",line.rstrip()],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout,stderr = response.communicate()
#print(stdout)
#print(stderr)
    if (response.returncode==0):
        status = line.rstrip() + " is reachable"
    else:
        status = line.rstrip() + " is not reachable"
    print(status)
    f.writelines(status + '\n')
f.close()
