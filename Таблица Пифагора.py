n, m = int(input()), int(input())
ma = []
for i in range(n):
    ma.append([0])
    if m > 1:
        ma[i].append(i)
for j in range(2, m):
    ma[0].append(0)
if m > 2:
    for j in range(2, m):
        ma[1].append(j)
if n > 0:
    for i in range(2, n):
        for j in range(2, m):
            ma[i].append(ma[i][1] * ma[1][j])
for i in range(len(ma)):
    for j in range(len(ma[i])):
        print(str(ma[i][j]).ljust(3), end='')
    print()
