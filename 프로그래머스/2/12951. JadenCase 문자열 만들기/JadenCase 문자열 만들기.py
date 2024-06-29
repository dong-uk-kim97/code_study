def solution(s):
    s = s.split(" ")
    temp = []
    for i in s:
        i = i.capitalize()
        temp.append(i)
    
    return " ".join(temp)