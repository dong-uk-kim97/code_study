from math import gcd
a,b =map(int,input().split())
print(gcd(a,b))
print(gcd(a,b)*(a//gcd(a,b))*(b//gcd(a,b)))