def solution(d, budget):
    d = sorted(d)
    answer = 0
    for i in d:
        if budget>=i:
            budget -=i
            answer +=1
    return answer