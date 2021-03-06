import subprocess

#p1 = subprocess.run(['ls','-al'])
#Print the output of ls-al in the console with args and returncode status with subprocess run.
#print(p1)
#Print the output in the console with args & returncode only with subprocess run.
#print(p1.args)
#print(p1.args[0])
#print(p1.args[1])
#print(p1.returncode)
#p2 = subprocess.run(['ls','-al'],capture_output=True,text=True)
# With Capture_output = True & No p2.stdout ,will not show any output to console.
#With capture_output = True & p2.stdout will show out in binary.
# With capture_output = True, p2.stdout.decode will show the output to console in text form.
# With capture_output = True & text = True, p1.stdout will show the output in text or string form.
# stdout=subprocess.PIPE will perform same function of capture_output=True
#p3 = subprocess.run(['ls','-al'],stdout=subprocess.PIPE,text=True)
#Without print p2.stdout, no output is shown in console.
#print(p3.stdout)
# Writing the output of cmd to to text file..
#with open('output.txt','w') as newfile:
 #   p3=subprocess.run(['ls','-al'],stdout=newfile,text=True)
  #  newfile.close()
# Capture Error output if dir doesn't exist but no output to console
#p4 = subprocess.run(['ls','-al','dne'],capture_output=True,text=True)
#print stderr output to console..
#print(p4.stderr)
#capture returncode as 1 if error exist
#print(p4.returncode)

#With check=True, python will throw exception error in console.
#p5 = subprocess.run(['ls','-al','dne'],capture_output=True,text=True,check=True)

# stderr=subprocess.DEVNULL perform same function as Capture_output = True . No out to console if print stderr.
p6 = subprocess.run(['ls','-al','dne'],stderr=subprocess.DEVNULL)
print(p6.stderr)