li = []
n = int(input())
for _ in range(n):
    a = int(input())
    li.append(a)
if li.count(0) > li.count(1):
    print("Junhee is not cute!")
elif li.count(0) < li.count(1):
    print("Junhee is cute!")