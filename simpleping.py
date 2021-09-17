#Reading list of Hostnames from hosts1.txt and printing ping response in different lines to hoststatus.txt
import os
import datetime
today = datetime.datetime.today()
filename = open('hosts1.txt','r')
#Using str for printing date in string format.
f = open('hoststatus_'+str(today)+'.txt','w')
lines = filename.readlines()
for line in lines:
    response = os.system("ping -c 1 "+ line)
    if (response == 0):
        status = line.rstrip() + " is reachable"
    else:
        status= line.rstrip()+ " is not reachable"
    f.writelines(status +"\n")
f.close()