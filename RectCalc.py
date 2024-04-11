class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Example usage:
rectangle1 = Rectangle(5, 4)  # Creating a Rectangle object with length 5 and width 4
print("Area of rectangle:", rectangle1.calculate_area())  # Calculating and printing the area
