"""
양의 정수 n이 매개변수로 주어집니다. 
n x n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
"""
    
def solution(n):
    # n x n 크기의 2차원 배열을 초기화합니다. 초기에는 모든 값이 None입니다.
    answer = [[None for j in range(n)] for i in range(n)]
    
    # 시계방향으로 움직이는 방향을 나타내는 리스트입니다. 오른쪽, 아래, 왼쪽, 위 순서입니다.
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    # 현재 위치 (x, y)와 현재 방향 m을 초기화합니다.
    x, y, m = 0, 0, 0
    
    # 1부터 n^2까지의 숫자를 배열에 배치합니다.
    for i in range(1, n**2 + 1):
        # 현재 위치에 i를 배치합니다.
        answer[y][x] = i
        
        # 다음 위치가 배열의 범위를 벗어나거나 이미 숫자가 배치된 경우, 방향을 바꿉니다.
        if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
            m = (m + 1) % len(move)
        
        # 현재 위치를 업데이트합니다.
        y, x = y + move[m][0], x + move[m][1]
    
    # 최종적으로 완성된 배열을 반환합니다.
    return answer