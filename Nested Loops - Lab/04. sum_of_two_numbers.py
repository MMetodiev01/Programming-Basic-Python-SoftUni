start = int(input())
final = int(input())
magic_number = int(input())
counter_of_combinations = 0
combinations_is_found = False

for first_number in range(start, final + 1):
    for second_number in range(start, final + 1):
        counter_of_combinations += 1
        if first_number + second_number == magic_number:
            combinations_is_found = True
            break
    if combinations_is_found:
        break
if combinations_is_found:
    print(f'Combination N:{counter_of_combinations} ({first_number} + {second_number} = {magic_number})')
else:
    print(f'{counter_of_combinations} combinations - neither equals {magic_number}')