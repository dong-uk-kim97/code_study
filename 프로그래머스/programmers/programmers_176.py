"""
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""

import math
def solution(numer1, denom1, numer2, denom2):
    """
    두 소수의 합을 계산하고 줄린 형태로 반환합니다.

    인자:
        numer1 (int): 첫 번째 소수의 분모입니다.
        denom1 (int): 첫 번째 소수의 분자입니다.
        numer2 (int): 두 번째 소수의 분모입니다.
        denom2 (int): 두 번째 소수의 분자입니다.

    반환:
        tuple: 두 소수의 합의 분모와 분자를 줄린 형태로 담은 튜플입니다.

    예시:
        >>> solution(1, 2, 3, 4)
        (7, 8)

    """
    numer = numer1*denom2 + numer2*denom1
    denom = denom1 * denom2
    gcd = math.gcd(numer,denom)
    
    return numer/gcd, denom/gcd