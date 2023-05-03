import sys

command = input()
max_num = -sys.maxsize

while command != "Stop":
    number = int(command)
    if max_num < number:
        max_num = number
    command = input()
    if command == "Stop":
        break
print(max_num)

