import math
a, b= map(int,input().split())
combi = math.comb(a,b)
combi %= 10007
print(combi)