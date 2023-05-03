import sys
command = input()
min_num = sys.maxsize

while command != "Stop":
    number = int(command)
    if min_num > number:
        min_num = number
    command = input()
    if command == "Stop":
        break
print(min_num)

# -10
# 20
# -30
# Stop