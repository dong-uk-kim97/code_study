"""
영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 
영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 
영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(score):
    avg = [sum(i)/2 for i in score] # 각 점수의 평균을 계산
    s_avg = sorted(avg, reverse=True) # 평균 점수를 내림차순으로 정렬

    answer =[] # 등수를 저장할 리스트
    for i in avg:
        answer.append(s_avg.index(i)+1) # 각 평균 점수의 등수를 계산하여 리스트에 추가
    
    return answer # 등수 리스트 반환