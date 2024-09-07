#include <stdio.h>
int main() {
    char se[1000];
    int i;
    
    scanf("%s",se);
    scanf("%d",&i);
    
    printf("%c",se[i-1]);
    return 0;
}