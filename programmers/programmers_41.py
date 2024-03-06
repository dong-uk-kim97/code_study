"""
정수가 담긴 리스트 num_list가 주어질 때, 
모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.
"""
from math import prod
def solution(num_list):
    return 1 if sum(num_list)**2 > prod(num_list) else 0