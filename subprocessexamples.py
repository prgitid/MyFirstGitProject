import subprocess

p1 = subprocess.run(['ls','-al'])
print(p1)
#print(p1.args[0])
#print(p1.returncode)
# With Capture_output = True & No p1.stdout ,will not show any output to console.
#With capture_output = True & p1.stdout will show out in binary.
# With capture_output = True, p1.stdout.decode will show the output to console in text form.
# With capture_output = True & text = True, p1.stdout will show the output in text or string form.
# stdout=subprocess.PIPE will perform same function of capture_output=True
#p2 = subprocess.run(['ls','-al'],stdout=subprocess.PIPE,text=True)
#Without print p2.stdout, no output is shown in console.
#print(p2.stdout)
# Writing the output of cmd to to text file..
#with open('output.txt','w') as newfile:
 #   p3=subprocess.run(['ls','-al'],stdout=newfile,text=True)
  #  newfile.close()
# Capture Error output if dir doesn't exist but no output to console
#p4 = subprocess.run(['ls','-al','dne'],capture_output=True,text=True)
# capture returncode as 1 if error is ther.
#print(p4.returncode)
#capture error in console.
#print(p4.stderr)
#With check=True, python will throw exception error in console.
#p5 = subprocess.run(['ls','-al','dne'],capture_output=True,text=True,check=True)