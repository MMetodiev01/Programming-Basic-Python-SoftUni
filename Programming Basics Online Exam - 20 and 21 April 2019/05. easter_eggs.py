eggs = int(input())

red_count = 0
orange_count = 0
blue_count = 0
green_count = 0
for i in range(1, eggs + 1):
    color = input()

    if color == "red":
        red_count += 1
    elif color == 'orange':
        orange_count += 1
    elif color == "blue":
        blue_count += 1
    elif color == "green":
        green_count += 1
max_value = max(red_count, orange_count, blue_count, green_count)
max_color = ""

if max_value == red_count:
    max_color = "red"
elif max_value == orange_count:
    max_color = "orange"
elif max_value == blue_count:
    max_color = "blue"
elif max_value == green_count:
    max_color = "green"

if i == eggs:
    print(f"Red eggs: {red_count}")
    print(f"Orange eggs: {orange_count}")
    print(f"Blue eggs: {blue_count}")
    print(f"Green eggs: {green_count}")
    print(f"Max eggs: {max_value} -> {max_color}")


