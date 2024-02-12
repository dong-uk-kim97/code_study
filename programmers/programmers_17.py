"""
중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 
예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 
정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.
"""
# 나의 풀이
import numpy as np
def solution(array):
    return np.median(array)

# 다른 사람의 풀이
def solution1(array):
    return sorted(array)[len(array)//2] # array를 정렬하여 새로 반환한 값 중에서 array의 총 갯수 중 가운데 있는 값(중앙값)을 반환함