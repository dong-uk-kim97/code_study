"""
문자열 my_string이 매개변수로 주어집니다. 
my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
"""

def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    my_string = my_string.split()
    
    return sum(list(map(int, my_string)))