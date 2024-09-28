import itertools

# 9명의 난쟁이 키 입력 받기
stack = []
for i in range(9):
    a = int(input())
    stack.append(a)

# 7명의 난쟁이 조합 중 합이 100인 조합 찾기
combs = itertools.combinations(stack, 7)
for comb in combs:
    if sum(comb) == 100:
        # 찾은 조합을 오름차순으로 정렬하여 출력
        result = sorted(comb)
        for height in result:
            print(height)
        break  # 첫 번째로 찾은 조합을 출력하고 종료
