def solution(new_id):
    # 1단계 : 문자열 자체를 소문자로 변환
    answer = new_id.lower() 
    # 2단계 : 지정된 문자를 제외한 나머지 문자를 전부 제거
    filtered = []
    for c in answer:
        if c.isalpha() or c.isdigit() or c in ('-','_','.'):
            filtered.append(c)
    answer = ''.join(filtered)
    # 3단계 : 마침표가 2번 찍혔다면 그중 하나만 제거
    while '..' in answer:
        answer = answer.replace('..','.')
    # 4단계 : 마침표 양옆으로 문자열을 제거
    answer = answer.strip('.')
    # 5단계 : 제거후, 아무것도 없다면 'a'할당
    if answer== '': answer ='a'
    # 6단계 : 나온 결과가 16자 이상일 경우 그 이상은 모두 삭제, 마지막 문자가 따옴표인 경우 역시 삭제
    if len(answer)>15: answer =answer[:15]
    if answer[-1]=='.': answer = answer[:-1]
    # 7단계 : 반대로 3자 미만이라면 마지막 문자를 반복해서 3글자 이상으로 만듦
    while len(answer)<3: 
        answer +=answer[-1]
    return answer