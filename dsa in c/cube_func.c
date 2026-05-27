#include<stdio.h>
void cube(){
    int a,b;
    printf("enter a:");
    scanf("%d",&a);
    b=a*a*a;
    printf("the cube of a no is %d\n",b);
}
int main()
{
    cube();
    return 0;
}