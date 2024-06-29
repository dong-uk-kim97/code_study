from math import gcd
def lcm(a,b):
  return (a * b) // gcd(a,b)
def solution(n, m):
    answer = [gcd(n,m), lcm(n,m)]
    return answer