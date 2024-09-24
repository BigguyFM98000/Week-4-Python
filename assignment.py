class Person:
    def __init__(self, name, age, gender):
        # Initializing the attributes
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        # Method to introduce the person
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.gender}.")

# Creating an instance of the Person class
person1 = Person("Alice", 30, "female")

# Calling the introduce method to display the person's information
person1.introduce()
