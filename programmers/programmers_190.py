"""
PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 
알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. 
spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 
존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.
"""

def solution(spell, dic):
    # dic 안의 각 요소에 대해 반복
    for i in dic:
        temp = []
        # i 안의 각 문자에 대해 반복
        for j in i:
            # temp 리스트에 문자를 추가
            temp.append(j)
        # temp 리스트 출력
        print(temp)
        # temp의 집합과 spell의 집합이 같다면
        if set(temp) == set(spell):      
            # 1을 반환
            return 1
    # 반복문이 끝나면 2를 반환
    return 2