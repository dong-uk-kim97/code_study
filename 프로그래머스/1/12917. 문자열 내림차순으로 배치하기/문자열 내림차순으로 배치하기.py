def solution(s):
    temp = []
    answer=''
    for i in s:
        temp.append(ord(i))
    temp = sorted(temp, reverse=True)
    for i in temp:
        answer +=chr(i)
    return answer