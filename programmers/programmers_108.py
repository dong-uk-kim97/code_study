"""
정수 배열 array가 매개변수로 주어질 때, 
가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""

def solution(array):
    answer = [max(array),array.index(max(array))] # 리스트.index()를 하면 그 요소의 index를 찾을 수 있음
    return answer