fruitToColor = {
    'banana': 'yellow',
    'blueberry': 'blue',
    'cherry': 'red',
    'lemon': 'yellow',
    'kiwi': 'green',
    'strawberry': 'red',
    'tomato': 'red'
}

colorToFruits = {}

for fruit, color in fruitToColor.items():
    if color not in colorToFruits:
        colorToFruits[color] = []
    colorToFruits[color].append(fruit)

for color, fruits in colorToFruits.items():
    print(f"{color}:{fruits}")