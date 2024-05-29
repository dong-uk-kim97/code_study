"""
문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(my_str, n):
    """
    주어진 문자열 `my_str`을 `n`글자씩 잘라서 부분 문자열로 나누어 반환합니다.
    
    Args:
        my_str (str): 분할할 입력 문자열입니다.
        n (int): 각 부분 문자열의 길이입니다.
    
    Returns:
        list: `n`글자씩 잘린 문자열의 부분 문자열 목록입니다. 빈 부분 문자열은 제거됩니다.
    """
    answer = []
    for i in range(0,len(my_str)//n+1):
        answer.append(my_str[n*i:(i+1)*n])
    return list(filter(None,answer))