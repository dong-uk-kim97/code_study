def solution(num):
    count = 0
    while num!=1:
        if num%2:
            num = 3*num +1
        else:
            num//=2
        count +=1
        if count ==500:
            return -1
    return count