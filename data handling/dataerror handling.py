## this uses try statements to sort out errors
"""The code opens a data file, processes each line in that file, extracts the data of
interest and displays it on screen. The file is closed when done. If any exceptions occur, this
code handles them."""
import os
os.chdir('/home/babu97/HeadFirstpython/chapter3')
man = []
other = []
try:
    data=open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)= each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role== 'Other Man':
                other.append(line_spoken)
            print(role, end='')
            print(' said: ' ,end='')
            print(line_spoken, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print ('The data file is missing!')
try:
    man_file =open('man_data.txt', 'w')
    other_file= open('other_data.txt', 'w')
    print(man, file=man_file)
    print(other, file=other_file)
    man_file.close()
    other_file.close()
except IOError:
    print('File error1.')



