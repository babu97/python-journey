## this uses try statements to sort out errors
import os
os.chdir('/home/babu97/HeadFirstpython/chapter3')
try:
    data=open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)= each_line.split(':',1)
            print(role, end='')
            print(' said: ' ,end='')
            print(line_spoken, end='')
        except:
            pass
except:
    print ('The data file is missing!')

data.close()

