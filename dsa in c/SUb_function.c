#include<stdio.h>
// return type functionname (parameter)
void subtraction(){
    int a,b,c;

    printf("enter a:");
    scanf("%d",&a);
    printf("enter b: ");
    scanf("%d",&b);
   
    c=a-b;

    printf("the subtraction is %d\n",c);    
}
int main()
{
    // function call
    subtraction();
    return 0;
}