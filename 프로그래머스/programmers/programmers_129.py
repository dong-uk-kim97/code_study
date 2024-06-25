"""
문자열 my_string과 정수 s, e가 매개변수로 주어질 때, 
my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, s, e):
    answer = my_string[:s]
    for i in range(e,s-1,-1):
        answer += my_string[i]
    answer +=my_string[e+1:]
    return answer