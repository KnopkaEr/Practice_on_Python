n = int(input())


def t_p(k):
    from math import factorial
    list1 = list([])

    for i in range(k+1):
        list1.append([1]+[0]*i)
    if k > 0:
        list1[1] = [1, 1]
        for i in range(2, k+1):
            for j in range(1, i):
                list1[i][j] = list1[i-1][j-1] + list1[i-1][j]
            list1[i][-1] = 1
    for i in range(k):
        print(*list1[i], sep=' ')
t_p(n)

