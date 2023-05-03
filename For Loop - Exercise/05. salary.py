tabs = int(input())
salary = int(input())

name_tab = input()
for i in range(1, tabs + 1):
    if name_tab == 'Facebook':
        salary -= 150
    elif name_tab == "Instagram":
        salary -= 100
    elif name_tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break
    if i == tabs:
        print(salary)
        break
    name_tab = input()




