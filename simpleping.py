
#Program for pinging the provided hostname or IP address with subprocess.
import subprocess
hostname=input("Enter IP Address or Website : ")
response = subprocess.Popen(["ping","-c","1",hostname.rstrip()],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

#Program for pinging localhost with subprocess.
#import subprocess
#response = subprocess.Popen(["ping","-c","1","localhost"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

stdout,stderr = response.communicate()
#print(stdout)
#print(stderr)
if (response.returncode==0):
    status = print(hostname.rstrip() + " is reachable")
else:
    status = print(hostname.rstrip() + " is not reachable")
