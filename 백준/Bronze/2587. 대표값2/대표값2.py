l = []
for i in range(5):
    m = int(input())
    l.append(m)
l.sort()
print(int(sum(l)/5))
print(l[2])