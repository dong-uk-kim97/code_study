#include <stdio.h>
int main()  {
    int sum = 0;
    int n;
    int i = 1;
    
    scanf("%d", &n);
    
    while (i<=n) {
        sum = sum + i;
        i++;
    } 
    printf("%d",sum);
    return 0;
}