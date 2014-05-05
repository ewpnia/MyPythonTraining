import os
import re

dir1 ='D:\\sztc2\\2013-11-12 OracleToInformix\\ii1'
dir2 ='D:\\sztc2\\2013-11-12 OracleToInformix\\ii2'


files = os.listdir(dir1)

for f in files:
    print f

    file1 = os.path.join(dir1,f)
    file2 = os.path.join(dir2,f)

    with open(file1, 'r') as f:
        with open(file2, 'w') as g:
            for line in f.readlines():
                if 'to_char' in line:  
                    pass
                elif 'time' in line:
                    pass
                elif 'TIME' in line:
                    pass
                else:           
                    g.write(line)
