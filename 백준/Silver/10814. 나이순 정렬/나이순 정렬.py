import sys
N = int(input())
li = []
for i in range(N):
    a,b = sys.stdin.readline().strip().split()
    li.append((int(a),b))
li.sort(key=lambda x :x[0])
for i in li:
    print(i[0], i[1])