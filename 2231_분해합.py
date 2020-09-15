n = int(input()) #256
result = list()
for i in range(n, 0, -1): #245+2+4+5 = 256인 245를 찾기
    temp = int(i)
    for ii in str(i):
        temp += int(ii)
    if temp == n:
        result.append(i)
if len(result) == 0:
    print(0)
else:
    print(min(result))