"""
정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(n):
    answer = [i for i in range(n+1) if i%2==1] # 홀수인 것만 포함을 하되 n=15일 때 본인도 포함해야하기 때문에 range(n+1)을 하여 15도 포함되게 한다.
    return answer