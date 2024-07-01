def solution(s):
    answer = ''
    s = s.split(' ')
    for i in s:
        for idx, val in enumerate(i):
            if idx%2==0:
                answer+=val.upper()
            else:
                answer +=val.lower()
        answer += ' '
            
    return answer[:-1]