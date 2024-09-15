import sys
input= sys.stdin.readline
a,b = map(int,input().split())
a_set = set(map(int,input().split()))
b_set = set(map(int,input().split()))
a_b = len(a_set) - len(a_set&b_set)
b_a = len(b_set) - len(b_set&a_set)
print(a_b + b_a)