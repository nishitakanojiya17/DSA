// recursion to print numbers
#include<stdio.h>

void fun(int num)
{
    if(num>1)

    {
        
        fun(num-1);
    }
    printf("%d ",num);
}
void main()
{
    fun(5); // 1 2 3 4 5
    fun(20);
}