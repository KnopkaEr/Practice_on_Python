n, k = int(input()), int(input())
p = [i for i in range(1, n+1)]
b = len(p)
for i in range(b-1):
    if k > len(p) > 0:
        n = k % len(p)
        if n == 0:
            p = p[:-1]
        else:
            p = p[n:] + p[:n-1]
    elif k == len(p):
        p = p[:-1]
    elif k < len(p):
        p = p[k:] + p[:k-1]
print(p[0])