class Mammal:
    def walk(self):
        print("Walk")


# We inherit from the Mammal class by passing its name through the brackets
# It will inherit all of the methods from its parent class
class Dog(Mammal):
    def bark(self):
        print("Bark")


# We inherit from the Mammal class by passing its name through the brackets
# It will inherit all of the methods from its parent class
class Cat(Mammal):
    # Tells python to don't worry about the class being empty
    pass


dog = Dog()
dog.walk()  # Prints walk
dog.bark()  # Calls the method we have created inside the dog class

cat = Cat()
cat.walk()  # Prints walk
