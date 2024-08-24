import sys
N = int(input())
for _ in range(N):
    sentence = sys.stdin.readline().split()
    for i in sentence:
        print(i[::-1], end=' ')