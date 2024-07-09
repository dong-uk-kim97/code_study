def solution(rows, columns, queries):
    answer = []
    # 가로 방향으로 1씩 증가하는 주어진 크기만큼의 행렬 생성
    board = [[columns*j + (i+1) for i in range(columns)] for j in range(rows)]
    # 회전해야 할 위치의 값을 받음
    for query in queries:
        # 파이썬은 0부터 시작하기 때문에 받아온 값에서 -1을 한다
        a, b, c, d = query[0]-1, query[1]-1, query[2]-1, query[3]-1 
        # 행렬을 시계 방향으로 회전 
        row1, row2 = board[a][b:d], board[c][b+1:d+1] # 가로 데이터를 슬라이싱으로 받아옴 
        _min = min(row1+row2) # 슬라이싱으로 나온 리스트를 합쳐서 가장 최소값을 _min에 받아옴
        # 세로 데이터 
        for i in range(c, a, -1): 
            board[i][d] = board[i-1][d]
            if board[i][d] <_min : _min = board[i][d]
        for i in range(a,c):
            board[i][b]=board[i+1][b]
            if board[i][b] < _min : _min = board[i][b]
            
        board[a][b+1:d+1], board[c][b:d] = row1, row2
        
        answer.append(_min)
        
    return answer