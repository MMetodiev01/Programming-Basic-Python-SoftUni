number = int(input())

left_side = 0
right_side = 0
for i in range(number):
    first_num = int(input())
    second_num = int(input())
    if i < 1:
        left_side = first_num + second_num
    else:
        right_side = first_num + second_num

if left_side != right_side:
    diff = abs(left_side - right_side)
    print(f"No, diff = {diff}")
else:
    print(f"Yes, sum = {first_num + second_num}")


