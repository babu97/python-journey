## this uses if else statement to check for and error instead of try statements

import os
os.chdir('/home/babu97/HeadFirstpython/chapter3')

data=open('sketch.txt')
for each_line in data:
    if not each_line.find(':') == -1:
        (role,line_spoken) = each_line.split(':',1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
data.close()