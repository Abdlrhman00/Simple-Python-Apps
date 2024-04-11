import math

def PointCalculator(speed, limit):
    difference = speed - limit
    points = math.floor(difference / 5)
    return points

def watchingU():
    speed = int(input("Enter speed: "))  # Convert input to integer

    if speed < 70:
        print("Ok")
    else:
        points = PointCalculator(speed, 70)
        print(f"Points: {points}")
        if points > 12:
            print("License suspended")

watchingU()
