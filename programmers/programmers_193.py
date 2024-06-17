"""
이차원 정수 배열 arr이 매개변수로 주어집니다. 
arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 
열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(arr):
    # 가장 긴 행의 길이와 전체 행의 수 중 더 큰 값을 찾음
    max_length = max(max(len(i) for i in arr), len(arr))

    # 각 행을 max_length에 맞게 확장
    for i in range(len(arr)):
        if len(arr[i]) < max_length:
            arr[i] += [0] * (max_length - len(arr[i]))

    # 필요한 경우 추가 행을 추가
    while len(arr) < max_length:
        arr.append([0] * max_length)

    return arr