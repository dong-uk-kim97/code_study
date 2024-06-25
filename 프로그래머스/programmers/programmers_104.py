"""
문자열 my_string이 매개변수로 주어집니다. 
my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
"""
def solution(my_string):
    answer = 0
    for i in my_string :
        if i.isdigit(): # isdigit 문자열에서 숫자를 판별하는 함수 return은 True / False로 반환
            answer += int(i)
            
    return answer