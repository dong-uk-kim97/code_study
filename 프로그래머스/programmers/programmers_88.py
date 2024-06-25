"""
문자열 myString이 주어집니다. 
"x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return 하는 solution 함수를 완성해 주세요.
단, 빈 문자열은 반환할 배열에 넣지 않습니다.
"""
def solution(myString):
    answer = list(filter(None, myString.split("x"))) # filter(None,리스트)를 하면 리스트 안에 빈 문자열 제거 
    return sorted(answer) # 새로운 정렬된 리스트 반환