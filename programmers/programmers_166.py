"""
정수 n과 정수 3개가 담긴 리스트 slicer 그리고 정수 여러 개가 담긴 리스트 num_list가 주어집니다. 
slicer에 담긴 정수를 차례대로 a, b, c라고 할 때, n에 따라 다음과 같이 num_list를 슬라이싱 하려고 합니다.

n = 1 : num_list의 0번 인덱스부터 b번 인덱스까지
n = 2 : num_list의 a번 인덱스부터 마지막 인덱스까지
n = 3 : num_list의 a번 인덱스부터 b번 인덱스까지
n = 4 : num_list의 a번 인덱스부터 b번 인덱스까지 c 간격으로
올바르게 슬라이싱한 리스트를 return하도록 solution 함수를 완성해주세요.
"""

def solution(n, slicer, num_list):
    """
    주어진 정수 `n`, 정수 리스트 `slicer`, 정수 리스트 `num_list`를 매개변수로 받아 리스트 `num_list`를 슬라이싱한 버전을 반환하는 함수입니다.

    매개변수:
    - n (int): 슬라이싱 방식을 나타내는 정수입니다.
    - slicer (list of ints): 슬라이싱에 사용될 시작과 끝 인덱스를 포함한 정수 리스트입니다.
    - num_list (list of ints): 슬라이싱할 정수 리스트입니다.

    반환값:
    - list of ints: `slicer`와 `n`의 값에 따라 `num_list`의 슬라이싱된 버전입니다.

    함수는 `n`의 값에 따라 다른 종류의 슬라이싱을 수행합니다.

    - `n`이 1이면, 함수는 `num_list`의 인덱스 0부터 `slicer[1] + 1`까지의 부분 리스트를 반환합니다.
    - `n`이 2이면, 함수는 `num_list`의 `slicer[0]`부터 끝까지의 부분 리스트를 반환합니다.
    - `n`이 3이면, 함수는 `num_list`의 `slicer[0]`부터 `slicer[1] + 1`까지의 부분 리스트를 반환합니다.
    - `n`이 4이면, 함수는 `num_list`의 `slicer[0]`부터 `slicer[1] + 1`까지의 부분 리스트를 `slicer[2]`의 간격으로 슬라이싱한 결과를 반환합니다.

    예시:
    ```
    n = 1
    slicer = [0, 2]
    num_list = [1, 2, 3, 4, 5]
    solution(n, slicer, num_list)  # 출력: [1, 2, 3]
            ```
    """
    if n==1:
       return num_list[:slicer[1]+1]
    elif n==2:
       return num_list[slicer[0]:]
    elif n==3:
       return num_list[slicer[0]:slicer[1]+1]
    elif n==4:
       return num_list[slicer[0]:slicer[1]+1:slicer[2]]    