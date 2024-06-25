"""
정수가 담긴 리스트 num_list가 주어질 때, 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.
"""
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(num_list)) # eval 함수는 문자열로 된 식의 값을 도출함 / '+'.join(num_list)는 리스트 요소들을 가운데 +를 넣어서 합침
    else:
        return eval('*'.join(num_list)) # '*'.join(num_list)는 리스트 요소들을 가운데 *를 넣어서 합침