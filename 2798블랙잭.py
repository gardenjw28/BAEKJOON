from itertools import combinations #조합함수
N, M = map(int, input().split())
card = list(map(int, input().split(' ')))
total_sum = 0
for i in combinations(card, 3): #card 조합들 갯수3개
    current_sum = sum(i)
    if total_sum < current_sum <= M:
        total_sum = current_sum
print(total_sum)