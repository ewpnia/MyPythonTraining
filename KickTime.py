    
import os
import re


dir1 ='D:\cbhb\\new'
dir2 ='D:\cbhb\NOTIME'

files = os.listdir(dir1)

for f in files:
    print f

    inputfile = os.path.join(dir1,f)
    outputfile = os.path.join(dir2,f)

    f = open(inputfile, "r")
    t = open(outputfile, "w")

    for line in f.readlines():
        if re.search(r'.time.',line):
            pass
        elif re.search(r'.TIME.',line):
            pass
        else:
            t.write(line)

    t.close()
    f.close()