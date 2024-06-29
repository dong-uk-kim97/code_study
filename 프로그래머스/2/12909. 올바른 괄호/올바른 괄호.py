def solution(s):
    stack = []
    
    #문자열 s크기만큼 반복  
    for i in s:
        if i == '(':
            stack.append('(')
        
        #')'일 경우
        else:
        	#스택이 빈 경우 ')'가 들어올 때
            if stack == []:
                return False
            
         	#스택 안에 '('가 있고 ')'가 들어와 올바른 괄호 
            else:
                stack.pop()
    
    #for문이 다 끝났는데도 '(' 괄호가 남아있는 경우
    if stack != []:
        return False
    
    return True