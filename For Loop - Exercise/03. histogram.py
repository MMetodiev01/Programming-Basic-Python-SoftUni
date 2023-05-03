n = int(input())

pt1 = 0
pt2 = 0
pt3 = 0
pt4 = 0
pt5 = 0

for i in range(1, n + 1):
    current_num = int(input())

    if current_num < 200:
        pt1 = pt1 + 1
    elif current_num <= 399:
        pt2 = pt2 + 1
    elif current_num <= 599:
        pt3 = pt3 + 1
    elif current_num <= 799:
        pt4 = pt4 + 1
    else:
        pt5 = pt5 + 1

pt1_percent = pt1 / n * 100
print(f'{pt1_percent:.2f}%')
pt2_percent = pt2 / n * 100
print(f'{pt2_percent:.2f}%')
pt3_percent = pt3 / n * 100
print(f'{pt3_percent:.2f}%')
pt4_percent = pt4 / n * 100
print(f'{pt4_percent:.2f}%')
pt5_percent = pt5 / n * 100
print(f'{pt5_percent:.2f}%')