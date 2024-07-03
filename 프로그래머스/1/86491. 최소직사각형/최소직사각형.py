def solution(sizes):
    # 1. 명함 지갑의 가로, 세로 길이 후보 list 변수 w, h 생성한다
    w = []  # 명함 지갑의 가로 길이 후보 리스트
    h = []  # 명함 지갑의 세로 길이 후보 리스트
    
    # 2. 주어진 명함들을 for 문을 돌면서 더 큰 값을 w, 작은 값을 h에 저장한다
    for size in sizes:
        if size[0] > size[1]:
            w.append(size[0])
            h.append(size[1])
        else:
            w.append(size[1])
            h.append(size[0])     
    
    # 3. 각 w, h 리스트에서 가장 큰 값을 곱한다
    return max(w) * max(h)