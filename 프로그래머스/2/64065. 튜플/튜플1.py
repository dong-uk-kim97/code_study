def solution(s):
    # answer 변수를 배열이 아니라 객체(딕셔너리)로 변경
    answer = {}
    # 문자열을 적절한 방법으로 쪼개고, 결괏값의 길이로 정렬
    s = sorted(s[2:-2].split("},{"), key=len)
    # 쪼갠 문자열을 한 번 더 "," 기준으로 쪼개 숫자가 있는 문자열을 찾음
    for tuples in s:
        elements = tuples.split(',')
        for element in elements:
            number = int(element)
            # 선착순으로 정답 객체에 할당하고, 중복을 확인하면서 루프를 진행한다.
            if number not in answer:
                answer[number] = 1
    return list(answer) # 딕셔너리를 list로 만들면 키 값만 리스트에 담겨진다.
