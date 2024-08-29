#include <stdio.h>
int main() {
    int a,b;
    scanf("%d", &a);
    scanf("%d", &b);
    
    int c = b/100;
    int d = (b%100)/10;
    int e = (b%100)%10;
    
    printf("%d \n",a*e);
    printf("%d \n",a*d);
    printf("%d \n", a*c);
    printf("%d", a*b);
    return 0;
}