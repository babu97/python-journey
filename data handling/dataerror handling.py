## this uses try statements
import os
os.chdir('/home/babu97/HeadFirstpython/chapter3')

data=open('sketch.txt')
for each_line in data:
    try:
        (role,line_spoken)= each_line.split(':',1)
        print(role, end='')
        print(' said: ' ,end='')
        print(line_spoken, end='')
    except:
        pass
data.close()

