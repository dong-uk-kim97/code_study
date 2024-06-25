"""
정수 배열 arr과 정수 n이 매개변수로 주어집니다. 
arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, 
arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.
"""
def solution(arr, n):
    for idx, val in enumerate(arr):
        if len(arr)%2==0:
            if idx%2==1:
                arr[idx]+=n
        else:
            if idx%2==0:
                arr[idx]+=n
    return arr