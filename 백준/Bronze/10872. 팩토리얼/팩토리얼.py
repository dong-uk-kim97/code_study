n = int(input())
answer=1
for i in range(n+1):
    if i==0 or i==1:
        answer*=1
    else:
        answer *=i
print(answer)