// wap to check string is palindrome or not 

#include<stdio.h>
#include<string.h>

void main()
{
    char str[50];
    printf("enter the string\n");
    gets(str);
    printf("original string is %s\n",str);
    
    char temp[50];
    strcpy(temp,str);
    strrev(str);
    printf("reverse of the string is %s\n",str);

    if(strcmp(temp,str)==0)
    {
        printf("string is palindrome\n");
    }
    else
    {
        printf("string is not palindrome\n");
    }

}