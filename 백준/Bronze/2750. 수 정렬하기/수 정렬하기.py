m = int(input())
l = []
for i in range(m):
    k = int(input())
    l.append(k)
l = sorted(l)
for i in l:
    print(i, end='\n')