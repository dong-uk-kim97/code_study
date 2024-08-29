#include <stdio.h>
/*
첫째 줄에 (A+B)%C
둘째 줄에 ((A%C) + (B%C))%C
셋째 줄에 (A×B)%C
넷째 줄에 ((A%C) × (B%C))%C
*/
int main(){
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%d \n", (a + b) % c);
    printf("%d \n", ((a % c) + (b % c)) % c);
    printf("%d \n", (a * b) % c);
    printf("%d \n", ((a % c) * (b % c)) % c);
    return 0;
}