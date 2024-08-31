#include <stdio.h>
int main() {
    int t,a,b;
    scanf("%d",&t);
    
    for(int i=1; i<=t; i++) {
        scanf("%d %d",&a,&b);
        if (a>0 && b<10){
            printf("Case #%d: %d\n",i,a+b);
        }
    }
    
    return 0;
}