"""
정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
"""

def solution(array, n):
    return array.count(n) # 배열에 정수 n의 갯수를 세는 것은 배열.count(n)을 사용한다.