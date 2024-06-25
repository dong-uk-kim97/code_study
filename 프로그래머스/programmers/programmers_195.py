"""
머쓱이는 RPG게임을 하고 있습니다. 
게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 
예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 
머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 
캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.

[0, 0]은 board의 정 중앙에 위치합니다. 
예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.
"""

def solution(keyinput, board):
    # 보드의 열과 행의 크기를 가져옵니다.
    col = board[0]
    row = board[1]
    
    # 현재 위치를 나타내는 리스트를 초기화합니다. 초기 위치는 (0, 0)입니다.
    result = [0, 0]
    
    # 입력된 키 명령에 따라 현재 위치를 업데이트합니다.
    for i in keyinput:
        # "left" 명령이고, 왼쪽으로 이동할 수 있는 경우
        if i == "left" and result[0]-1 >= -(col // 2):
            result[0] -= 1
        # "right" 명령이고, 오른쪽으로 이동할 수 있는 경우
        elif i == "right" and result[0]+1 <= (col // 2):
            result[0] += 1
        # "up" 명령이고, 위쪽으로 이동할 수 있는 경우
        elif i == "up" and result[1]+1 <= (row // 2):
            result[1] += 1
        # "down" 명령이고, 아래쪽으로 이동할 수 있는 경우
        elif i == "down" and result[1]-1 >= -(row // 2):
            result[1] -= 1
    
    # 최종적으로 계산된 위치를 반환합니다.
    return result