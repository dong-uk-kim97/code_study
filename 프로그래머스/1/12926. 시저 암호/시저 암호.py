def solution(s, n):
    s = list(s)  # 문자열 s를 리스트로 변환
    
    for i in range(len(s)):  # s의 각 문자에 대해 반복
        if s[i].isupper():  # 해당 문자가 대문자인 경우
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))  # 대문자를 n만큼 이동
        elif s[i].islower():  # 해당 문자가 소문자인 경우
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))  # 소문자를 n만큼 이동

    return "".join(s)  # 리스트를 문자열로 변환하여 반환
