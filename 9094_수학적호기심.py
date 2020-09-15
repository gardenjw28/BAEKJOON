from itertools import combinations
T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    numList = list(map(int, [i for i in range(1,n)]))
    numList = list(combinations(numList, 2))
    total = 0
    for p in numList:
        a, b = p[0], p[1]
        num = (a**2 + b**2 + int(m))/(a*b)
        if num.is_integer():
            total += 1
    print(total)