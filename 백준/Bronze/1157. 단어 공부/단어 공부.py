word = input().lower() # 입력 받은 문자열을 소문자로 변경
word_list = list(set(word)) # 문자열을 집합에 넣고 중복을 제거 후 리스트에 삽입
cnt = [] # 카운트를 세기 위한 리스트

for i in word_list: # 반복문을 통해 집합에 있는 알파벳을 i에 하나씩 추가
    count = word.count(i) # i에 해당하는 알파벳을 하나씩 word 문자열에서 뺌
    cnt.append(count) # word 문자열에서 뺀 알파벳을 cnt에 추가

if cnt.count(max(cnt)) >= 2: #가장 많은 알파벳이 2개 이상이면 ? 출력
    print('?')
else:
    print(word_list[(cnt.index(max(cnt)))].upper()) # 그렇지 않으면 대문자로 출력