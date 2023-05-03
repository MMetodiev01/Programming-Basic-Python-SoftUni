budget = int(input())

statues = budget * 0.70
catering = statues * 0.85
voicing = catering / 2
total = statues + catering + voicing + budget
print(f"{total:.2f}")