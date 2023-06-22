def addition ():
 while True:
    try:
        number1 = input("Please Enter a  First_Number of Your Choice(enter Q to quit\n)")
        if number1.lower() == 'q':
           break

        number2 = input("Please Enter a second_number to be added")
        if number2.lower() == 'q':
           break
        number1 = int(number1)
        number2  = int(number2)

    except ValueError:
    
        print("The number entered is not of type Integer please correct")
    

    sum = number1 + number2
    print( "Sum:",sum )


addition()





    





