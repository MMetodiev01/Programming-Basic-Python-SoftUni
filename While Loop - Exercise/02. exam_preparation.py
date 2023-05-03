poor_grade = int(input())
sum_grade = 0
input_line = input()
count_grades = 0
last_problem = ""
count_poor_grades = 0
while input_line != "Enough":
    grade = int(input())
    if grade <= 4:
        count_poor_grades += 1
    if count_poor_grades == poor_grade:
        break
    count_grades += 1
    sum_grade += grade
    last_problem = input_line

    input_line = input()
if count_poor_grades == poor_grade:
    print(f'You need a break, {count_poor_grades} poor grades.')
else:
    average_grade = sum_grade / count_grades
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {count_grades}')
    print(f'Last problem: {last_problem}')



# 2
# Income
# 3
# Game Info
# 6
# Best Player
# 4