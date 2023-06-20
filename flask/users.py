class User:
    def __init__(self,first_name,last_name,age,location,occupation, login_attempts) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = login_attempts


    def describe_user(self):
        print(f"This is the user information")
        print(f"Full name {self.first_name} {self.last_name}")
        print(f"Age {self.age}")
        print(f"Location{self.location}")
        print(f"occupation {self.occupation}")


    def greet_user(self):
        print(f"Welcome to this portal - {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
  def __init__(self, first_name, last_name, age, location, occupation, login_attempts) -> None:
      super().__init__(first_name, last_name, age, location, occupation, login_attempts)

      self.privileges = []
  def show_privileges(self):
      
      for privilege in self.privileges:
          print(privilege)
          




# Creating instances of the User class
user1 = User("John", "Doe", 30, "New York", "Software Engineer")
user2 = User("Alice", "Smith", 25, "San Francisco", "Graphic Designer")
user3 = User("Bob", "Johnson", 35, "London", "Business Analyst")

# Calling the methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
