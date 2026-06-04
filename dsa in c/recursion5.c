// wap to make a function  which take a nuumber and return sum of individual digits of that number  

#include<stdio.h>
int digitsum(int num) //56 
{
    if(num==0)
    {
        return 0;
    }
    else
    {
        return(num%10 + digitsum(num/10)); // 6 + digitsum(5) => 6 + 5 + digitsum(0) => 6 + 5 + 0 => 11
    }
}
void main()
{
    printf("sum of digit= %d",digitsum(56));
}