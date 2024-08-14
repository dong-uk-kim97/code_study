def solution(n, times):
    # 1. 0분부터 가장 오래 걸리는 소요 시간을 시작과 끝으로 지정
    answer = 0
    left, right = 1, max(times) * n
    
    # 2. 시작과 끝의 중간 시간에서 최대 몇 명 심사할 수 있을지 계산
    while left <= right:
        mid = (left+right) // 2
        people = 0
        test = []
        
        for time in times:
            people += mid//time
            if people >= n: break
    
    # 3. 심사해야 할 사람의 숫자보다 많으면 끝의 크기를 줄이고, 적으면 시작의 크기를 줄여 이진 탐색을 수행
        if people >=n:
            answer = mid
            right = mid -1
        elif people < n:
            left = mid + 1
            
    return answer