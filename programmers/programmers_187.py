"""
영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 
문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
"""

def solution(numbers):
    # 숫자를 영어로 표현한 리스트
    nums = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]

    # 각 숫자에 대해
    for i, num in enumerate(nums):
        # 해당 숫자의 영어 표현을 찾아서 숫자로 바꾼다.
        numbers = numbers.replace(num,str(i))

    # 모든 변환이 끝난 후 문자열을 숫자로 변환하여 반환한다.
    return int(numbers)