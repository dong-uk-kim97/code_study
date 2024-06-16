"""
2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 
직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 
직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.
"""

def solution(dots): 
    # dots 리스트에서 x 좌표의 최대값과 최소값의 차이를 구하여 가로 길이 w를 계산
    w = max(dots)[0] - min(dots)[0]
    # dots 리스트에서 y 좌표의 최대값과 최소값의 차이를 구하여 세로 길이 h를 계산
    h = max(dots)[1] - min(dots)[1]
    # 가로 길이 w와 세로 길이 h를 곱하여 직사각형의 넓이 area를 계산
    area = w*h
    # 계산된 넓이 area를 반환
    return area