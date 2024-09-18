import sys
input=sys.stdin.readline

n = int(input())

sum_ = 0
for i in range(1, n+1):
	# i의 배수의 개수 = i를 약수로 갖는 수
    sum_ += (n//i)*i

print(sum_)