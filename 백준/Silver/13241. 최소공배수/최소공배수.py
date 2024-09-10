from math import gcd
a,b = map(int,input().split())
g = gcd(a,b)
if g==1:
    print(a*b)
else:
    print((a//g)*(b//g)*g)