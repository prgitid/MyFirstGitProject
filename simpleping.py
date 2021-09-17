#Reading list of Hostnames from hosts1.txt and printing ping response in different lines to filename with timedate
import os
import datetime
#using strftime for printime timestamp in format dd mm yy hour and second..
today = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
filename = open('hosts1.txt','r')
#concatenating filename with script running date
f = open('hoststatus_'+today+'.txt','w')
lines = filename.readlines()
for line in lines:
    response = os.system("ping -c 1 "+ line)
    if (response == 0):
        status = line.rstrip() + " is reachable"
    else:
        status= line.rstrip()+ " is not reachable"
    f.writelines(status +"\n")
f.close()