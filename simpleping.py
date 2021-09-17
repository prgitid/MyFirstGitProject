#Program for pinging localhost with subprocess.
import subprocess
response = subprocess.Popen(["ping","-c","1","localhost"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
stdout,stderr = response.communicate()
#print(stdout)
#print(stderr)
if (response.returncode==0):
    status = print("localhost is reachable")
else:
    status = print("localhost is not reachable")

