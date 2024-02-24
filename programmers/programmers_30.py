"""
정수 리스트 num_list와 정수 n이 주어질 때, 
n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.
"""
def solution(num_list, n):
    return num_list[n-1:] # n번째 원소를 담으려면 인덱스는 1작기 때문에 n-1로 줘야 함