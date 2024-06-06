"""
0 이상의 두 정수가 문자열 a, b로 주어질 때, a + b의 값을 문자열로 return 하는 solution 함수를 작성해 주세요.
"""

def solution(a, b):
    # 문자열 a와 b를 '+' 연산자로 연결하여 수식을 만듭니다.
    # eval 함수를 사용하여 이 수식을 평가하고, 그 결과를 문자열로 변환하여 반환합니다.
    return str(eval(a+'+'+b))