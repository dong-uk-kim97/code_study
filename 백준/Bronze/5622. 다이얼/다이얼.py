LS =['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

S= input()
time = 0
for s in S:
    for idx, ls in enumerate(LS):
        if s in ls:
            time +=(idx+3)
            
print(time)