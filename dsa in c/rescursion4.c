//return 1 to given no sum

#include<stdio.h>

void sum(int num)
{
   int sum=0,i;
   for(i=1;i<=num;i++)
   {
        sum=sum+i;
   }
   printf("Sum of numbers from 1 to %d is: %d", num, sum);
}

void main()
{
    sum(20); 
}

// factorial 
//even sum
// odd sum 
// 