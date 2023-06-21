with open('pi_digit.txt') as file_object:
    lines  = file_object.readlines()


pi_string  = ''
for line in lines:

    line1 =  line.replace('python', 'c')
    pi_string += line1.rstrip()

print (pi_string)

print (len(pi_string))









