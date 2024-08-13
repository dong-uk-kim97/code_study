from itertools import permutations
import re
        
def solution(user_id, banned_id):
    answer = set()
    banned = ' '.join(banned_id).replace('*','.')
    for i in permutations(user_id, len(banned_id)):
        if re.fullmatch(banned, ' '.join(i)):
            answer.add(''.join(sorted(i)))
    
    return len(answer)
