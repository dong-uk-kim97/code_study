N,M = map(int, input().split())

# 행렬 초기화
A,B = [],[]

# A행렬
for i in range(N):
    a = list(map(int,input().split()))
    A.append(a)
# B행렬        
for i in range(N):
    b = list(map(int,input().split()))
    B.append(b)
# 행렬의 덧셈
for i in range(N):
    for j in range(M):
        result = A[i][j] + B[i][j]
        print(result,end=' ')
    print()