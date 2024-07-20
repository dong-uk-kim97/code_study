def febo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return febo(n-2)+febo(n-1)
n= int(input())
print(febo(n))