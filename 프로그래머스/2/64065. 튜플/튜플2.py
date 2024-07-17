def solution(s):
    # 첫 중괄호를 제거하고 분리 기준을 잡는다.
    data = s[2:-2].split("},{")
    # 튜플의 조건을 맞춰 쪼개진 문자열을 길이에 맞게 정렬한다.
    data = sorted(data, key=lambda x:len(x))
    answer = []
    # 쪼갠 문자열을 한 번 더 ','기준으로 쪼개진 숫자가 있는 문자를 찾는다.
    for item in data:
        # 중괄호를 제거한 숫자 문자열 -> 문자열을 숫자로 변환 -> 숫자
        item = list(map(int, item.split(',')))
        for value in item:
            # 선착순으로 정답 배열에 할당하고, 중복을 확인하면서 루프를 진행한다.
            if value not in answer:
                answer.append(value)
    return answer
