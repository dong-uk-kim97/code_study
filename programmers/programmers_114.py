"""
정수가 담긴 리스트 num_list가 주어질 때, 
num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""

def solution(num_list):
    answer = []
    count_o = 0
    count_e = 0
    for i in num_list:
        if i%2==0:
            count_e+=1
        else:
            count_o+=1
    return [count_e, count_o]