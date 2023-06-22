import json 
"""Load the username, if it has been stored previously.
 Otherwise, prompt for the username and store it"""
def greet_user():
    """Greet the user by name"""
    filename  = 'username.json'
    try:
        with open(filename) as f:
            username  = json.load(f)
    except FileNotFoundError:
        username = input("what is your username?")
        with open(filename, 'w') as f:
            username = json.dump(f)
        print(f"We'll remember you when you come back, {username}")
    else:
        print(f"welcome back, {username}")
greet_user()