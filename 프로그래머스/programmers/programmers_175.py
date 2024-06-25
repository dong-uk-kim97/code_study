"""
이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.
"""

def solution(bin1, bin2):
    """
    두 개의 이진 숫자를 문자열로 표현하고 그 합을 문자열로 반환합니다.

    인자:
        bin1 (str): 첫 번째 이진 숫자.
        bin2 (str): 두 번째 이진 숫자.

    반환:
        str: 두 이진 숫자의 합을 문자열로 표현합니다.

    예제:
        >>> solution("1010", "1011")
        '10101'
    """
    a = int(bin1, 2) # int(,2) 이진수을 10진수로 변환
    b = int(bin2, 2)
    answer = bin(a+b) # 10진수을 이진수로 변환
    return answer.replace("0b","") # 0b 제거 후 이진수로 return