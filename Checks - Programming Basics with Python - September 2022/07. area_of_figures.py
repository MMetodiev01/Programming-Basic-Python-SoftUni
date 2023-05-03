from math import pi

type_of_figures = input()
result = 0

if type_of_figures =='square':
    side = float(input())
    result = side * side
elif type_of_figures == 'rectangle':
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side
elif type_of_figures == 'circle':
    radius = float(input())
    result = pi * (radius ** 2)
elif type_of_figures == 'triangle':
    side = float(input())
    height = float(input())
    result = side * height / 2
print(f'{result:.3f}')
