n,m = map(int,input().split())
l = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int,input().split())
    l[i-1],l[j-1] =l[j-1],l[i-1]
for s in l:
    print(s, end=' ')