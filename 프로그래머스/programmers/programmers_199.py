"""
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
"""
def solution(quiz):
    answer = []  # 정답을 저장할 리스트 초기화
    for i in quiz:  # 퀴즈 리스트의 각 문제에 대해 반복
        a = eval(i.split("=")[0])  # '=' 기호를 기준으로 분리한 후, 첫 번째 부분(수식)을 계산
        b = int(i.split("=")[1].strip())  # '=' 기호를 기준으로 분리한 후, 두 번째 부분(정답)을 정수로 변환
        if a == b:  # 계산된 결과와 주어진 정답이 같으면
            answer.append('O')  # 'O'를 정답 리스트에 추가
        else:  # 계산된 결과와 주어진 정답이 다르면
            answer.append('X')  # 'X'를 정답 리스트에 추가
    return answer  # 최종 정답 리스트 반환