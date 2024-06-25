"""
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
"""

def solution(numbers):
    answer = sorted(numbers)
    return max(answer[0]*answer[1],answer[-1]*answer[-2]) 
# 정렬하면 음수 중 절댓값이 크면 index가 0,1로 갈 것이고 양수 중 절댓값이 크면 index가 -1,-2로 가기 때문에 두 개 곱한 것 중 큰 값을 return 한다.