from itertools import combinations
N,M = map(int,input().split())
cards = list(map(int,input().split()))
score = []
for i in combinations(cards,3):
    if sum(i)<=M:
        score.append(sum(i))
print(max(score))
    