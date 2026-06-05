#include<stdio.h>
#include<string.h>

struct moouse
{
    //structure is a user defined data type which can hold different types of data
    char name[30];
    char color[10];
    int price;  
    int rating;
};

void main()
{
    struct moouse m1,m2,m3;
    //assigning values to m1
    strcpy(m1.name,"Logitech");
    strcpy(m1.color,"Black");
    m1.price=500;
    m1.rating=4;
    
    printf("Mouse 1 details:\n");
    printf("Name: %s\n",m1.name);
    printf("Color: %s\n",m1.color);
    printf("Price: %d\n",m1.price);
    printf("Rating: %d\n",m1.rating);


    //assigning values to m2
    strcpy(m2.name,"HP");
    strcpy(m2.color,"White");
    m2.price=300;
    m2.rating=3;

    printf("\nMouse 2 details:\n");
    printf("Name: %s\n",m2.name);
    printf("Color: %s\n",m2.color);
    printf("Price: %d\n",m2.price);
    printf("Rating: %d\n",m2.rating);
}