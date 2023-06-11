#store information about a pizza being ordered 
pets = {
    
        'rex':{
            'First': 'Albert', 
            'Last':'Einstein',
            'location':'Kabarbet',
            'age':20
        },
        'Mcurie':{
            'First':'Kipkulei',
            'Last':'Ben',
            'location':'Paris',
            'age':7
        },
    
}
for pet,details in pets.items():
  
  print (f"username: {pet.capitalize()}")
  
  full_name  = f"{details['First']}  {details['Last']}"
  kutoka= f"{details['location']}"
  miaka = f"{details['age']}"

  print(f"\tFull Name: {full_name.title()}")
  print (f"\tLocation:{kutoka.title()}")
  print (f"\t age:{miaka.title()}")

  

