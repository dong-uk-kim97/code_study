def hanoi(n, start, to, mid, answer):
    if n==1:
        return answer.append([start, to])
    hanoi(n-1, start, mid, to, answer) # 1개 남을 때까지 시작에서 경유지로 옮김
    answer.append([start, to]) # 목적지로 옮김
    hanoi(n-1, mid, to, start, answer) # 1개 남을 때까지 시작지로 옮김

def solution(n):
    answer = []
    hanoi(n,1,3,2,answer)
    return answer