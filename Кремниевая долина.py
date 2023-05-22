n = int(input())
a = ['a', 'n', 't', 'o', 'n']
numbers = []
f = True
for i in range(n):
    s = input()
    k = j = 0
    while k < len(s) and j < 5:
        if s[k] == a[j]:
            j = j + 1
        k = k + 1
    if j == 5:
        numbers.append(i+1)
print(*numbers, sep=' ')