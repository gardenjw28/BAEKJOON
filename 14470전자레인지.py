A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
totalTime = 0
if A < 0 :
    totalTime = (0 - A)*C + D
    totalTime += B*E
elif A == 0:
    totalTime = D + B * E
else : # A >0
    totalTime = (B - A) * E
print(totalTime)