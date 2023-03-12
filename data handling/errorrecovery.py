## this uses if else statement to check for and error instead of try statements
"""The code  starts by importing the “os” library, and then it uses “path.exists” to
make sure the data file exists, before it attempts to open the data file. Each line from
the file is then processed, but only after it has determined that the line conforms to the
required format by checking first for a single “:” character in the line. If the “:” is found,
the line is processed; otherwise, it’s ignored. When we’re all done, the data file is closed. And
you get a friendly message at the end if the file is not found."""
import os
os.chdir('/home/babu97/HeadFirstpython/chapter3')
if os.path.exists('sketch.txt'):
    data=open('sketch.txt')
    for each_line in data:
        if not each_line.find(':') == -1:
            (role,line_spoken) = each_line.split(':',1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
else:
    print(' error!! 404: file not found !! please check provided')

data.close()