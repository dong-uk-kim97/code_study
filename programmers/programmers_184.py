"""
직사각형 형태의 그림 파일이 있고, 이 그림 파일은 1 x 1 크기의 정사각형 크기의 픽셀로 이루어져 있습니다. 
이 그림 파일을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질 때, 
이 그림 파일을 가로 세로로 k배 늘린 그림 파일을 나타내도록 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
"""
    
def solution(picture, k):
    # 결과를 저장할 빈 리스트를 초기화합니다.
    answer = []
    
    # picture의 각 행에 대해 반복합니다.
    for i in picture:
        # 각 행을 확대할 임시 문자열을 초기화합니다.
        temp = ''
        # 행의 각 문자에 대해 반복합니다.
        for j in range(len(i)):
            # 각 문자를 k번 반복하여 temp에 추가합니다.
            temp += i[j] * k
        # 확대된 행을 k번 반복하여 answer에 추가합니다.
        for _ in range(k):
            answer.append(temp)
    # 최종적으로 확대된 그림을 반환합니다.
    return answer