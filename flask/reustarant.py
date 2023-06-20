class Restaurant:
    def __init__(self, restaurant_name, cuisine_type,number_served,):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

    def increment_number_served(self,increment):
        self.number_served +=increment
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors  = []

    def  display_flavors(self):
        for flavor in self.flavors:
            print (flavor)






# Creating an instance of the IceCreamStand class
ice_cream_stand = IceCreamStand("Scoop and Joy", "Ice Cream")

# Adding flavors to the ice cream stand
ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chip"]

# Calling the display_flavors() method
ice_cream_stand.display_flavors()
