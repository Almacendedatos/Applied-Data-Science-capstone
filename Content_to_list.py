# import of libraries
import os

# Request for data
path = input(" directory path :")
name = input(" Name for the file :")

completeName = os.path.join(path, name+".txt")   

# obtain list of files and directories into the results file


with open(completeName, 'w') as f:
  for root, dirs, files in os.walk(path):
    for i in files:
        f.write("%s\n" % i)
    for j in dirs:
        f.write("%s\n" % j)
        
      
 
