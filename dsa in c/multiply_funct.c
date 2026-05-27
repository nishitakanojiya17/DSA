#include<stdio.h>

void multiply(){
    int a,b,c;
    printf("enter a:");
    scanf("%d",&a);
    printf("enter b:");
    scanf("%d",&b);
    c=a*b;
    printf("the multiplication is %d\n",c);

}
int main(){
    multiply();
    return 0;
    
}