import sys

n = int(input())

sum = 0
max_num = -sys.maxsize

for i in range(1, n + 1):
    current_num = int(input())

    sum = sum + current_num
    if current_num > max_num:
        max_num = current_num

other_nums = sum - max_num
if other_nums == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    diff = abs(other_nums - max_num)
    print(f'Diff = {diff}')

