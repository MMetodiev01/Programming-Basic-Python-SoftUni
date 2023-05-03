n = int(input())
sum = 0
for i in range(n + 1):
    if i == n:
        break
    current_num = int(input())
    sum += current_num
average_sum = sum / n
print(f'{average_sum:.2f}')