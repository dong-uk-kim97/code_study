from collections import deque
import sys
N = int(input())
deque2 = deque()
for _ in range(N):
    a = sys.stdin.readline().split()
    if a[0] == "1": deque2.appendleft(a[1])
    elif a[0] == "2": deque2.append(a[1])
    elif a[0] == "3": print(deque2.popleft() if deque2 else -1)
    elif a[0] == "4": print(deque2.pop() if deque2 else -1)
    elif a[0] == "5": print(len(deque2))
    elif a[0] == "6": print(0 if deque2 else 1)
    elif a[0] == "7": print(deque2[0] if deque2 else -1)
    elif a[0] == "8": print(deque2[-1] if deque2 else -1)