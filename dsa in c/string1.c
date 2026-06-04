//strcmp()- compare two  string 
// string built in function 

#include <stdio.h>
#include <string.h>

void main()
{
   char a[50]="nishita";
   char b[40]="kanojiya";
   printf("string a is %s\n",a);
   printf("string b is %s\n",b);
   printf("compare of the string is %d \n",strcmp(a,b)); 
   // data same hota hai toh 0 return hoga 
   // data different hota hai toh 1 return hoga 

   // with if else condition 
   if (strcmp(a,b)==0)
   {
    printf("string is same\n");
   }
   else
   {
    printf("string is different\n");
   }
}