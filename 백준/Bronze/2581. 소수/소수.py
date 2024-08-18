n = int(input())
m = int(input())
min_v = m
sum = 0
for i in range(n, m+1):
  cnt = 0
  if i != 1:
    for j in range(2, int(i**(1/2))+1):
      if i%j==0: 
        cnt = 1
        break
    if not cnt:
      sum += i
      min_v = min(min_v, i)
if sum:
  print(sum)
  print(min_v)
else:
  print(-1)