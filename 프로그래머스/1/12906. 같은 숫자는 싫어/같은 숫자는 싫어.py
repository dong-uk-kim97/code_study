def solution(arr):
    answer = []
    for i in arr:
        if answer == []:
            answer.append(i)
        elif answer[-1]!=i:
            answer.append(i)
        elif answer[-1]==i:
            continue
    return answer