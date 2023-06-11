responses = {}
poling_active =True
while poling_active:
    name = input(f"\nWhat is your name Buddy?")
    response  = input(f"\n Which mountains have you climbed lately buddy!")

    responses[name] = response
    repeat  = input(f"Would you like to add another's person's details (YES/NO) ?")

    if repeat ==('no'):
        poling_active =False

print("\n Polling is complete and the following are the results!")



for name,response in responses.items():
    print(f"\n {name} has climbed {response} mountains this Year ! conratulations bro ")


