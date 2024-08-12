def solution(genres, plays):
    # 1. 데이터를 분할하여 조건에 맞게 정리
    answer = []
    info = {}
    gens = {}
    
    for idx,(gen,play) in enumerate(zip(genres, plays)):
        if gen not in info:
            info[gen] = [(idx,play)]
        else:
            info[gen].append((idx,play))
            
        gens[gen] = gens.get(gen,0) + play
    
    # 2. 데이터를 정렬하여 문제의 조건에 맞게 탐색
    
    for (gen, _) in sorted(gens.items(), key = lambda x: x[1], reverse=True):
        for (idx, _) in sorted(info[gen], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(idx)
    return answer