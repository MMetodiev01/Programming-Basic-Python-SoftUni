import math

easter_bread = int(input())

most_sugar = 0
most_flour = 0
count_sugar = 0
count_flour = 0

for i in range(1, easter_bread + 1):
    sugar = int(input())
    flour = int(input())

    count_sugar += sugar
    count_flour += flour
    if sugar > most_sugar:
        most_sugar = sugar

    if flour > most_flour:
        most_flour = flour

    if i == easter_bread:
        break
count_package_sugar = count_sugar / 950
count_package_flour = count_flour / 750

print(f"Sugar: {math.ceil(count_package_sugar)}")
print(f"Flour: {math.ceil(count_package_flour)}")
print(f"Max used flour is {most_flour} grams, max used sugar is {most_sugar} grams.")