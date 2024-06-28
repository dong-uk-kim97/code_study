from math import sqrt
def solution(n):
    answer = 0
    if sqrt(n).is_integer():
        answer = sqrt(n) +1
        return answer **2

    return -1