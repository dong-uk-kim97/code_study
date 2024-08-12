def collatz(num,answer):
    if num == 1: return answer # 시작 입력 숫자가 1일때 / 결과가 1일 때 모두 확인
    if answer == 500: return -1
    
    # 짝수
    if num%2==0:
        return collatz(num//2, answer+1)
    
    # 홀수
    elif num%2==1:
        return collatz(num*3 + 1, answer+1)

def solution(num):
    return collatz(num,0)