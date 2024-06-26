def solution(line):
    meet = list()  # 교점을 저장할 리스트
    x_max = y_max = -float('inf')  # x, y의 최대값 초기화
    x_min = y_min = float('inf')  # x, y의 최소값 초기화
    
    # 모든 선분의 조합을 확인하여 교점을 찾음
    for i in range(len(line)):
        a, b, e = line[i]  # 첫 번째 선분의 계수
        for j in range(i+1, len(line)):
            c, d, f = line[j]  # 두 번째 선분의 계수
            # 두 선분이 평행한 경우 건너뜀
            if ((a*d)-(b*c)) == 0:
                continue
            # 교점의 x, y 좌표 계산
            x = ((b*f)-(e*d)) / ((a*d)-(b*c))
            y = ((e*c)-(a*f)) / ((a*d)-(b*c))
            # 교점의 좌표가 정수인 경우에만 처리
            if x.is_integer() and y.is_integer():
                x = int(x)
                y = int(y)
                meet.append([x,y])  # 교점 리스트에 추가
                # x, y의 최대/최소값 업데이트
                x_max, y_max = max(x_max, x), max(y_max, y)
                x_min, y_min = min(x_min, x), min(y_min, y)
                
    # 별을 그릴 영역의 너비와 높이 계산
    width = abs(x_max - x_min) + 1
    height = abs(y_max - y_min) + 1
    # 별을 그릴 영역 초기화
    answer = [['.']*width for _ in range(height)]
    # y 좌표에 따라 교점을 정렬 (y 좌표가 큰 교점부터 처리하기 위함)
    meet = sorted(meet, key=lambda i: -i[1])
    
    # 교점에 별을 찍음
    for x, y in meet:
        ny = y_max - y  # 실제 그림에서의 y 좌표
        nx = x - x_min  # 실제 그림에서의 x 좌표
        answer[ny][nx] = "*"  # 별 찍기
        
    return list(map(''.join, answer))  # 2차원 리스트를 문자열 리스트로 변환하여 반환