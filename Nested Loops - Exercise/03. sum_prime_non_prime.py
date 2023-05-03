sum_of_prime_number = 0
sum_of_non_prime_number = 0
command = input()
while command != 'stop':
    current_number = int(command)  #взимаме си следващо число щом не е 'стоп'
    if current_number < 0:
        print('Number is negative.')
    else:
        current_number_is_prime = True
        for number in range(2, current_number):
            if current_number % number == 0:
                current_number_is_prime = False
                break
        if current_number_is_prime:      #if current_number_is_prime = True
            sum_of_prime_number += current_number
        else:
            sum_of_non_prime_number += current_number

    command = input()
print(f'Sum of all prime numbers is: {sum_of_prime_number}')
print(f'Sum of all non prime numbers is: {sum_of_non_prime_number}')

# 3
# 9
# 0
# 7
# 19
# 4
# stop