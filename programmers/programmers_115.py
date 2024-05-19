"""
문자열 my_string과 두 정수 m, c가 주어집니다. 
my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

my_string	            m	c	result
"ihrhbakrfpndopljhygc"	4	2	"happy"
"programmers"	        1	1	"programmers"
"""

def solution(my_string, m, c):
    answer = my_string[c-1::m]
    return answer