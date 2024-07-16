def solution(arr1, arr2):
    # 피연산자(arr1)와 연산자(arr2)의 크기만큼 행렬을 생성한다.
    # arr1의 행 개수와 arr2의 열 개수를 기준으로 결과 행렬의 크기를 결정
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    # arr1의 각 행을 순회
    for i in range(len(arr1)):
        # arr2의 각 열을 순회
        for j in range(len(arr2[0])):
            # arr1의 크기만큼 순회
            for k in range(len(arr1[0])):
                # 행렬의 곱셈을 수행하여 결과 행렬의 각 원소를 계산
                # arr1의 i행 k열 원소와 arr2의 k행 j열 원소를 곱하여 누적
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    
    # 계산된 결과 행렬을 반환
    return answer