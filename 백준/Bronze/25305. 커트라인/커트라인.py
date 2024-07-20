n,k = map(int,input().split())
x=map(int,input().split())
print(sorted(x,reverse=True)[k-1])