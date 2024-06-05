"""
0과 1로만 이루어진 정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk을 만드려고 합니다.

i의 초기값을 0으로 설정하고 i가 arr의 길이보다 작으면 다음을 반복합니다.

만약 stk이 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
stk에 원소가 있고, stk의 마지막 원소가 arr[i]와 같으면 stk의 마지막 원소를 stk에서 제거하고 i에 1을 더합니다.
stk에 원소가 있는데 stk의 마지막 원소가 arr[i]와 다르면 stk의 맨 마지막에 arr[i]를 추가하고 i에 1을 더합니다.
위 작업을 마친 후 만들어진 stk을 return 하는 solution 함수를 완성해 주세요.

단, 만약 빈 배열을 return 해야한다면 [-1]을 return 합니다.
"""

def solution(arr):
    # 빈 리스트를 생성하여 스택으로 사용합니다.
    answer = []

    # 입력 배열의 각 요소에 대해 반복합니다.
    for i in range(len(arr)):
        # 스택이 비어있으면 현재 요소를 스택에 추가합니다.
        if len(answer)==0:
            answer.append(arr[i])
        else:
            # 스택의 최상단 요소가 현재 요소와 같으면 스택의 최상단 요소를 제거합니다.
            if arr[i] == answer[-1]:
                answer.pop()
            # 스택의 최상단 요소가 현재 요소와 다르면 현재 요소를 스택에 추가합니다.
            elif arr[i] != answer[-1]:
                answer.append(arr[i])

    # 모든 요소를 처리한 후 스택이 비어있으면 -1을 추가합니다.
    if len(answer)==0:
        answer.append(-1)

    # 최종 스택을 반환합니다.
    return answer