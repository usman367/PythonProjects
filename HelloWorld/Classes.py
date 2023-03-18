import self as self

# Because the functions are part of classes now, we refer to them as methods

# Simple example:
# class Point:
#     # Declaring a variable
#     x = 0
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# # Creating an object of our class
# point = Point()
# point.draw()  # Calling its draw function
# point.x = 10  # Changing the vale of its variable x
# print(point.x)


# With a constructor:
class Point:

    #  Creating its constructor
    # Self is a reference to the current object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# Creating an object of our class
point = Point(10, 20)
print(point.x)