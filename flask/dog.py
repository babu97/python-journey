class Car:
    def __init__(self,make, model, year, manufacturer) -> None:
        self.make  = make
        self.model = model
        self.year =year
        self.manufacturer = manufacturer
        self.odometer_reading  = 30

    def  get_descriptive_name(self):

        """Return self descriptive name about the car"""

        long_name  = f"{self.make} {self.year} {self.manufacturer} {self.model} "
        return long_name.title()
    
    def read_odometer(self):
        """Print statement to show car mileage"""

        print(f"This car has {self.odometer_reading} miles on it ")

    def update_odometer(self,mileage):
      """set the odometer reading to the given value.
      Reject the change if it attemts to roll the odometer back."""
      if  mileage>= self.odometer_reading:
          self.odometer_reading = mileage
      else:
          print("You can't roll back an odometer!")
    def increase_odometer(self,miles):
        """Add the given amount to the odome if miles >= self.odometer_reading:
         self.odometer_reading += milester reading."""
        if miles > 0:
          self.odometer_reading += miles 
        else:
            print("You are not allowed to add a negative value!")
          



my_new_car = Car('Audi', ' a4',2019, 'Audi Technoogies')

my_new_car.increase_odometer(1)

#my_new_car.update_odometer(201)

print (my_new_car.get_descriptive_name())
my_new_car.read_odometer()

class Battery:
    """A simple attempt to model a battery for an electric car"""


    def __init__(self, battery_size =75) :
        self.battery_size= battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}- Kwh battery")
    def get_range(self):
        """Print a statment about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} Miles on a full charge.")
    def upgrade_battery(self):

          """check the battery size and set to 100 if its not set"""

          if self.battery_size < 100:
              self.battery_size = 100




class Electricar(Car):
    """Represents aspect of a car, specific to electric Vehicles."""

    def __init__(self,make,model,year,manufucturer):
        """initialize attributes of the parent class."""

        super().__init__(make,model,year, manufucturer)
        self.battery = Battery()


    def describe_battery(self):
        """Print a statemnt"""
        print(f"This car has a {self.batery_size} -kwh battery.")

my_tesla = Electricar('Tesla', 'Model s' , 2019, 'Tesla')


print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
#my_tesla.battery.get_range()






        
        





