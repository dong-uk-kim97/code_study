"""
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in ['a','e','i','o','u']:
            answer+=i
    return answer