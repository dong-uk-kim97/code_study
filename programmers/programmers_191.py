"""
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 
최빈값이 여러 개면 -1을 return 합니다.
"""

def solution(array):
    # array의 길이가 0이 아닐 때까지 반복
    while len(array) != 0:
        # array의 각 요소에 대해 반복
        for i, a in enumerate(set(array)):
            # array에서 해당 요소를 제거
            array.remove(a)
        # 만약 i가 0이라면 a를 반환
        if i == 0: return a
    # 반복문이 끝나면 -1을 반환
    return -1