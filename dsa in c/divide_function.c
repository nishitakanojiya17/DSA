#include <stdio.h>
void divide(){
    int a,b,c;
    printf("enter a:");
    scanf("%d",&a);
    printf("enter b:");
    scanf("%d",&b);
    c=a/b;
    printf("the division is %d\n",c);
}
int main(){
    divide();
    return 0;   
}