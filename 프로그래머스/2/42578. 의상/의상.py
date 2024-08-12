def solution(clothes):
    # 경우의 수를 곱하기 위해 변수 초기화
    answer = 1
    cloth_type = {}
    
    # 받은 옷을 종류별로 구분하여 해시 테이블 작성
    for cloth, types in clothes:
        cloth_type[types] =cloth_type.get(types,0) + 1
    
    for types in cloth_type:
        answer *= (cloth_type[types]+1)
    
    return answer-1