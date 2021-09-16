import os
filename = open('hosts1.txt','r')
lines = filename.readlines()
for line in lines:
    response = os.system("ping -c 1 "+ line)
    if (response == 0):
        status = line.rstrip() + " is reachable"
    else:
        status= line.rstrip()+ " is not reachable"
    print(status)
