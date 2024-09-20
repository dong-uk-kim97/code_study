N = int(input())

# 입력받은 학생들을 [5,4,1,3,2]의 리스트 형태로 바꿔준다.
students = list(map(int, input().split())) 

stack = []

now_turn = 1
for student in students:
	# 대기열 한명 스택으로
    stack.append(student)
    # 보낼 수 있는지 확인하고 보낸다. 
    # 스택이 비어있지 않다면 마지막 요소와 현재 차례를 비교
    while stack and stack[-1] == now_turn:
        stack.pop() # 차례 학생이라면 스택에서 빼고
        now_turn +=1 # 다음 차례로 저장한다.

# 반복문을 전부 돌았는데 스택에 요소가 남았다면 더 이상 진행이 불가능한 것이므로
if stack: 
    print('Sad') 
else:
    print('Nice')