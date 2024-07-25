n = int(input())
a=b=100
for _ in range(n):
    c,d = map(int,input().split())
    if c<d:
        a-=d
    elif c>d:
        b-=c
    elif c==d:
        continue
print(a)
print(b)