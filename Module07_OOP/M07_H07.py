### Homework 7: Object-Oriented Programming (OOP) in Python
## In this homework we will create a superclass Rectangle and subclass Square

### Problem 1: Define a class called Rectangle that contains:
# attributes height and width 
# methods area() and perimeter() 

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

## Use case: Create an instance of the Rectangular class and call the area and perimeter methods to verify that they work correctly.
my_rectangle = Rectangle(5, 3)
print("Area of rectangle", my_rectangle.area())
print("Perimeter of rectangle", my_rectangle.perimeter())

### Problem 2: Define a subclass called Square that 
# inherits from parent class Rectangle
# Using super(), will set .height and .width attributes from inherited superclass Rectangle.__init__()
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
 
## Use case: Create an instance of the Square class and call the area and perimeter methods to verify that they work correctly.
my_square = Square(5)
print("Area of square", my_square.area())
print("Perimeter of square", my_square.perimeter())
### Problem 3: Create a new class Cube that inherits from parent class Square
# Use super() to set .height and .width attributes from inherited superclass Square.__init__()
# Define new methods surface_area() and volume() that calculate the surface area and volume of the cube using the inherited attribute 

class Cube(Square):
    def __init__(self, side):
        super().__init__(side)

    def surface_area(self):
        return 6 * self.area()

    def volume(self):
        return self.height ** 3

## Use case: Create an instance of the Cube class and call the surface_area and volume methods to verify that they work correctly.
my_cube = Cube(5)
print("Surface area of cube", my_cube.surface_area())
print("Volume of cube", my_cube.volume())
