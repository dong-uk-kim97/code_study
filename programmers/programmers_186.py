"""
머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다. 
공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 
친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.
"""

def solution(numbers, k):
    answer = 0
    # 만약 numbers의 길이가 k의 2배보다 작다면,
    # numbers를 (k*2) // len(numbers) + 1 만큼 반복하여 numbers를 확장합니다.
    if len(numbers) < k * 2:
        numbers = numbers * ((k*2) // len(numbers) + 1)

    # numbers에서 2*(k-1) 위치의 값을 answer로 설정합니다.
    answer = numbers[2*(k-1)]
    return answer  # answer를 반환합니다.