"""
정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
"""

def solution(n):
    data=list()
    for i in range(n+1):
        if i % 2 == 0:
            data.append(i)
    return sum(data)


# 리스트 컨프리헨션을 사용할 풀이

def solution(n):
    data=[i for i in range(n+1) if i%2==0]
    return sum(data)   