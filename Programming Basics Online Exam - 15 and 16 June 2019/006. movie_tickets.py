a1 = int(input())
a2 = int(input())
n = int(input())
sim1 = a2 - 1
sim2 = n - 1
sim3 = int(n / 2 - 1)
for i in range(a1, sim1 + 1):
    for j in range(1, sim2 + 1):
        for k in range(1, sim3 + 1):
            if i % 2 != 0 and (i + j + k) % 2 != 0:
                print(f"{chr(i)}-{j}{k}{i}")
