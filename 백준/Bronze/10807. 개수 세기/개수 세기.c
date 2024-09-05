#include <stdio.h>
 
int main() {
 
    int n;            // 몇개의 수를 입력할건지
    int a[100];       // 수 입력
    int v;            // 입력받은수 중에 v가 있는지
    int cnt = 0;     // 개수 카운트
 
    scanf("%d", &n);
 
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
 
    scanf("%d", &v);
 
    for (int j = 0; j < n; j++) {
        if (a[j] == v)    // 입력받은 수들중 v와 같다면
            cnt++;        // cnt로 카운트 
    }
 
    printf("%d", cnt);
}
