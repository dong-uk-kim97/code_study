"""
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 
네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

네 주사위에서 나온 숫자가 모두 p로 같다면 1111 x p점을 얻습니다.
세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 x p + q)2 점을 얻습니다.
주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) x |p - q|점을 얻습니다.
어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q x r점을 얻습니다.
네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
"""

def solution(a, b, c, d):
    # 주사위의 숫자를 리스트에 담는다.
    dice_list = [a, b, c, d]
    # 중복되지 않은 숫자만 추출한다.
    non_dup_list = list(set(dice_list))
    # 중복된 숫자가 없는 경우
    if len(non_dup_list) == 1:
        return 1111 * non_dup_list[0]
    # 중복된 숫자가 두 개인 경우
    elif len(non_dup_list) == 2:
        # 3개의 숫자가 동일한 경우
        for element in dice_list:
            if dice_list.count(element) == 3:
                p = element
                q = [x for x in non_dup_list if x != p][0]
                return (10*p+q)**2
        # 2개의 숫자가 동일한 경우
        for element in dice_list:
            if dice_list.count(element) == 2:
                p = element
                q = [x for x in non_dup_list if x != p][0]
                return (p + q)*(abs(p-q))
    # 중복된 숫자가 세 개인 경우
    elif len(non_dup_list) == 3:
        for element in dice_list:
            if dice_list.count(element) == 2:
                new_list = [x for x in non_dup_list if x != element]
                return new_list[0]*new_list[1]
    # 중복된 숫자가 없는 경우
    else:  
        return min(dice_list)
