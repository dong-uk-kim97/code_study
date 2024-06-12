"""
머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 구슬은 모두 다르게 생겼습니다. 
머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, 
balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.
"""

import math

def solution(balls, share):
    # math 모듈의 comb 함수를 사용하여 조합을 계산한다.
    return math.comb(balls,share)

"""
Python의 math.comb(n, k) 함수는 n개의 아이템 중에서 k개를 선택하는 조합의 수를 계산합니다. 
이 함수는 정확히 두 개의 인자를 받으며, 첫 번째 인자는 전체 아이템의 수(n), 두 번째 인자는 선택할 아이템의 수(k)를 나타냅니다. 
이 함수는 조합의 수를 정수로 반환합니다.
"""