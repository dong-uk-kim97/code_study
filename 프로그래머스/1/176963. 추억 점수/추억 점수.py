def solution(name, yearning, photo):
    # 1. 반환할 결괏값 선언과 이름과 그리움 점수를 묶어준다.
    result = []
    info = dict(zip(name, yearning))
    
    # 2. 사진 속 사람들을 확인할 for loop
    for people in photo:
        
        # 3. 그리움 점수 누적을 위한 변수 선언
        score = 0
        
        # 4. 사람들 각각의 점수를 확인할 for loop
        for person in people:
            # 5. 사람 별 점수를 누적, 없는 사람은 0
            score += info.get(person, 0)
        # 6. 결과 배열에 담아주기
        result.append(score)
    
    return result