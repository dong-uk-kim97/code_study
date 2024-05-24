"""
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 
정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.
"""

def solution(array):
    answer = 0
    for i in array:
        for j in str(i):
            if "7" in str(j):
                answer +=1
    return answer
