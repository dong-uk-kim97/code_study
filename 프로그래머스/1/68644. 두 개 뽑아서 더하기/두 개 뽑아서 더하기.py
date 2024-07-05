from itertools import permutations
def solution(numbers):
    answer = []
    for i in permutations(numbers,2):
        answer.append(sum(i))
    return sorted(list(set(answer)))