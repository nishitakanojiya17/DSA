// string built in function 

#include <stdio.h>
#include <string.h>

void main()
{
    char name[50]="nishita";
    char name1[40]="kanojiya";
    printf("original string is %s\n",name);
    printf("length of the string is %d\n",strlen(name));
    printf("upper case string is %s \n ",strupr(name));
    printf("lower case string is %s \n ",strlwr(name));
    //printf("reverse of the string is %s \n",strrev(name));
    printf("concated string is %s \n", strcat(name,name1));
    printf("copy of the string is %s \n",strcpy(name,name1));
    // printf("compare of the string is %d \n",strcmp(name,name1));
}