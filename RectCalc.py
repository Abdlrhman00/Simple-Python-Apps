class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width


width = int(input("Enter width: "))
height = int(input("Enter height: "))

rectangle1 = Rectangle(height, width)
print("Area of rectangle:", rectangle1.calculate_area()) 
