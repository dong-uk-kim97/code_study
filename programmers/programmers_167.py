"""
외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 
정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(emergency):
    """
    주어진 정수 배열 `emergency`를 내림차순으로 정렬하고, 각 요소의 인덱스를 정렬된 배열에서 몇 번째인지 나타내는 새로운 배열을 반환합니다.

    매개변수:
    - `emergency` (정수 배열): 응급 수준을 나타내는 배열입니다.

    반환값:
    - `answer` (정수 배열): 각 요소가 정렬된 배열에서의 인덱스에 1을 더한 값을 나타내는 배열입니다.
    """
    answer = []
    temp = sorted(emergency, reverse = True)
    for i in emergency:
        answer.append(temp.index(i) + 1)
    return answer