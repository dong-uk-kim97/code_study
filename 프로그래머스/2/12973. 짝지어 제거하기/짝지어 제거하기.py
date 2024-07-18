def solution(s):
    # 스택 초기화
    stack = [] 
    # 받을 문자열을 for문으로 1글자씩 읽음
    for case in s:
        # 만약 배열의 마지막 알파벳과 현재 순회 중인 알파벳이 같다면
        if stack and stack[-1]==case:
            # 배열에서 해당 요소 제거
            stack.pop()
        else:
            # 배열에 알파벳을 넣음 
            stack.append(case)
    # 모든 문자열을 다 돌았을 때 배열에 값이 없다면 모두 짝지은 것이고, 남아 있다면 모두 짝짓지 못한 것이다.
    return 0 if stack else 1