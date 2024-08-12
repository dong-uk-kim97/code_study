def solution(record):
    # 1. 정답 배열, 과정 배열, 유저 데이터를 저장할 딕셔너리를 정의
    answer = []
    actions = [] 
    user = {} # 반복해서 탐색과 수정이 이루어지기 때문에 딕셔너리 사용
    
    # 2. 명령을 하나씩 따라가면서 유저의 닉네임 정보를 계속 변경
    for event in record:
        info = event.split()
        cmd, uid = info[0], info[1]
        if cmd in ("Enter", "Change"):
            nick = info[2]
            user[uid] = nick
    
        actions.append((cmd,uid))
    
    # 3. 한 번 더 명령줄을 따라가면서 출입 기록을 저장
    for action in actions:
        cmd, uid = action
        if cmd == "Enter":
            answer.append(f'{user[uid]}님이 들어왔습니다.')
        elif cmd == 'Leave':
            answer.append(f'{user[uid]}님이 나갔습니다.')

    return answer