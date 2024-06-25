"""
문자열 배열 strArr이 주어집니다. 
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.
"""

def solution(strArr):
    """
    주어진 문자열 리스트 `strArr`에서 같은 길이를 갖는 문자열의 개수를 세어서, 가장 많이 등장하는 길이의 개수를 반환합니다.
    
    매개변수:
    - `strArr` (list): 문자열 리스트입니다.
    
    반환값:
    - `int`: `strArr` 안의 문자열들 중에서 가장 많이 등장하는 길이의 개수입니다.
    """
    answer = [len(i) for i in strArr]
    tmp = []
    for i in set(answer):
        tmp.append(answer.count(i))
    
    return max(tmp)