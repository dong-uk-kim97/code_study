"""
알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, 
my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수,
my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string):    
    """
    주어진 문자열 `my_string`에 포함된 대문자와 소문자의 빈도를 계산합니다. 
    각 문자의 ASCII 값을 인덱스로 하는 길이가 52인 리스트를 반환합니다. 
    인덱스는 A-Z와 a-z의 ASCII 값을 나타내고, 해당 인덱스의 값은 `my_string`에서 해당 문자의 빈도를 나타냅니다.

    Parameters:
    - my_string (str): 분석할 입력 문자열입니다.

    Returns:
    - answer (List[int]): 길이가 52인 리스트입니다. 
      인덱스는 A-Z와 a-z의 ASCII 값을 나타내고, 해당 인덱스의 값은 `my_string`에서 해당 문자의 빈도를 나타냅니다.
    """
    answer = [0 for i in range(52)]
    for string in my_string:
        if string.isupper(): k = 65
        else: k = 71
        answer[ord(string)-k] += 1
    return answer