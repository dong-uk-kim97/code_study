"""
정수 리스트 num_list와 정수 n이 주어질 때, 
num_list의 첫 번째 원소부터 마지막 원소까지 n개 간격으로 저장되어있는 원소들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
"""
def solution(num_list, n):
    return num_list[::n] # 간격 n만큼의 원소들을 담은 리스트 return