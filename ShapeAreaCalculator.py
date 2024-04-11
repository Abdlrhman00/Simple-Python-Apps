class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


def calculate_rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle = Rectangle(length, width)
    print("Area of rectangle:", rectangle.calculate_area())

def calculate_square_area():
    side_length = float(input("Enter the side length of the square: "))
    square = Square(side_length)
    print("Area of square:", square.calculate_area())

while True:
    print("Choose an option:")
    print("1. Calculate area of rectangle")
    print("2. Calculate area of square")
    print("3. Quit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        calculate_rectangle_area()
    elif choice == '2':
        calculate_square_area()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
