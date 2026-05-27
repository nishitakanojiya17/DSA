#include<stdio.h>
//addition - function name
void addition()
{
    int a,b,c;
    printf("enter a:");
    scanf("%d",&a);
    printf("enter b:");
    scanf("%d",&b);
    c=a+b;
    printf("the sum is %d\n",c);
}
void main()
{
    //function calling 
    addition();
}