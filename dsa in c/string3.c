// check palindrome string 
#include<stdio.h>
#include<string.h>

void main()
{
    char str[50]="naman"; //5
    int i,j,f;
    i=0;
    j=strlen(str)-1; //4
    f=1;
    
    while(i<j) // 0<4 1<3 2<2
    {
        if(str[i]!=str[j])
        {
            f=0; // 0 0 1
            printf("string is not palindrome\n");
            return;
        }
        i++; // 1 2
        j--; // 3 2
    }
    if(f==1)
    {
        printf("string is palindrome\n");
    }
}