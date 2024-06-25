"""
문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.
"""

def solution(myString, pat):    
    start = 0
    cnt = 0
    
    while True:
        idx = myString.find(pat, start)
        if idx == -1:
            break
        cnt += 1
        start = idx + 1
    
    return cnt