def solution(a, b, n):
    answer = 0
    while (n >= a):
        remain_bottle = n % a
        n = (n//a) * b # 마트에서 받은 콜라의 수
        answer += n # 받은 걸 answer에 +
        n += remain_bottle # 남아있는 병을 더해줘서 다음에 마트갈 때 이용
    return answer