number = int(input())

odd_sum = 0
even_sum = 0

for i in range(1, number + 1):
    current_number = int(input())

    if i % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

diff = abs(odd_sum - even_sum)
if even_sum == odd_sum:
    print(f'Yes ')
    print(f'Sum = {even_sum}')
else:
    print(f'No')
    print(f'Diff = {diff}')



