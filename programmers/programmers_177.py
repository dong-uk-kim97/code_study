"""
문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다. 
str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 
먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요. 
"l"이나 "r"이 없다면 빈 리스트를 return합니다.
"""

def solution(str_list):
    """
    이 함수는 문자열 리스트를 입력받아서 새로운 문자열 리스트를 반환합니다. 함수는 입력 리스트를 반복하면서 리스트 내의 문자열이 "l"이나 "r"인지 확인합니다.
    "l"이 발견되면 함수는 입력 리스트에서 "l"이 위치한 이전 문자열들로 구성된 새로운 리스트를 반환합니다. 
    "r"이 발견되면 함수는 입력 리스트에서 "r"이 위치한 이후의 문자열들로 구성된 새로운 리스트를 반환합니다. 
    "l"이나 "r"이 발견되지 않으면 함수는 빈 리스트를 반환합니다.

    매개변수:
    - str_list (list of str): 처리할 문자열 리스트.

    반환값:
    - new_list (list of str): 조건에 따라 생성된 새로운 문자열 리스트.
    """
    for i in range(len(str_list)):
        if str_list[i] == "l":
            return str_list[:i]
        elif str_list[i] == "r":
            return str_list[i+1:]
    
    return []