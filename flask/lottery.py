import random 

numbers  = ['a', 'b', 'c', 'd','e',1,2,3,4,5,6,7,8,9,10]


ticker_selection = random.sample(numbers,4)
print (ticker_selection)

## check if any ticket matches the four selections

if set(ticker_selection).intersection(set(numbers[:10])) and set(ticker_selection).intersection(set(numbers[10:])):


   print ("Congratulations you have a winning Ticket")
else:
   print("Sorry, you ticket did not win a Ticket")




   