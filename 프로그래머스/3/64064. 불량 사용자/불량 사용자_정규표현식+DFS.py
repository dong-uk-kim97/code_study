import re

def search(idx, visit, user_id, answer, banPatterns):
    if idx == len(banPatterns):
        answer.add(visit)
        return
    
    for i in range(len(user_id)):
        if (visit & (1 << i) > 0 or not re.fullmatch(banPatterns[idx], user_id[i])):
            continue
        search(idx+1, visit | (1<<i), user_id, answer, banPatterns)
        
def solution(user_id, banned_id):
    answer = set()
    banPatterns = [x.replace('*','.') for x in banned_id]
    search(0,0,user_id, answer, banPatterns) 
    
    return len(answer)
