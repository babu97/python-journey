try: 
    with open('myfile.txt') as me:
        her = me.read()
    print(her)
except FileNotFoundError:
    print (' The file was not found near that place')
except PermissionError:
    print ('You are not allowed to modify this problem men ')

except Exception as err: 
    print('some other error occurred:', str(err))