"""
정수 배열 arr가 주어집니다. 
배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.

단, arr에 2가 없는 경우 [-1]을 return 합니다.
"""

def solution(arr):
    """
    주어진 정수 배열 `arr`에서 2의 두 개의 발생을 포함하는 부분 배열을 반환합니다. 
    만약 배열에 2의 두 개의 발생이 없을 경우, 함수는 [-1]을 반환합니다.

    매개변수:
    - arr (list): 정수 배열.

    반환값:
    - list: `arr`의 두 개의 2의 발생을 포함하는 부분 배열이거나, 2의 두 개의 발생이 없을 경우 [-1]을 반환합니다.
    """
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2):len(arr) - arr[::-1].index(2)]