## this uses try statements to sort out errors
"""The code opens a data file, processes each line in that file, extracts the data of
interest and displays it on screen. The file is closed when done. If any exceptions occur, this
code handles them."""
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
        except ValueError:
            pass
except IOError:
    print ('The data file is missing!')

data.close()

