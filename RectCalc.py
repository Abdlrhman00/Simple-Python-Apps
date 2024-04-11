class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


rectangle1 = Rectangle(5, 4)  
print("Area of rectangle:", rectangle1.calculate_area()) 
