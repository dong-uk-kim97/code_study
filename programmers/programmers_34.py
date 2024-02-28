"""
어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 
예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix)) # startswith함수는 문자열 앞에 있는 문자가 있는지 확인하는 문자 return은 boolean으로 한다.
# 그래서 int(boolean)하면 True면 1, False면 0의 값이 나온다.