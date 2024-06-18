"""
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

 - 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
 
삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 
나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요
"""

def solution(sides):
    # 결과를 저장할 변수를 초기화합니다.
    answer = 0
    
    # 주어진 변 중에서 가장 긴 변을 찾습니다.
    max_side = max(sides)
    
    # 주어진 변 중에서 가장 짧은 변을 찾습니다.
    min_side = min(sides)
    
    # sides에 있는 변(max_side)이 가장 길 경우, 삼각형을 만들 수 있는 새로운 변의 길이를 계산합니다.
    for new_side in range (max_side - min_side + 1, max_side + 1):
        # 가능한 새로운 변의 길이마다 answer를 1씩 증가시킵니다.
        answer += 1
        
    # 새로운 변(new_side)이 가장 길 경우, 삼각형을 만들 수 있는 새로운 변의 길이를 계산합니다.
    for new_side in range (max_side + 1, max_side + min_side):
        # 가능한 새로운 변의 길이마다 answer를 1씩 증가시킵니다.
        answer += 1
        
    # 최종적으로 계산된 가능한 새로운 변의 길이의 개수를 반환합니다.
    return answer