import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"Rolling a {self.sides}-sided die:")
        for  i in range(10):
            result = random.randint(1, self.sides)
            print(result)
        

# Create a 6-sided die
six_sided_die = Die()
six_sided_die.roll_die()

# Create a 10-sided die
ten_sided_die = Die(sides=10)
ten_sided_die.roll_die()

# Create a 20-sided die
twenty_sided_die = Die(sides=20)
twenty_sided_die.roll_die()
