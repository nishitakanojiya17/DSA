#include<stdio.h>
#include<string.h>

struct student 
{
    char name[30];
    int roll_no;
    float marks;
};
// function to display student details
void displaystudent(struct student s)
{
    printf("Name: %s\n",s.name);
    printf("Roll No: %d\n",s.roll_no);
    printf("Marks: %.2f\n",s.marks);
}

void main()
{
    struct student s1,s2;

    strcpy(s1.name,"nishita ");
    s1.roll_no=101;
    s1.marks=95.5;

    printf("Student 1 details:\n");
    printf("Name: %s\n",s1.name);
    printf("Roll No: %d\n",s1.roll_no);
    printf("Marks: %.2f\n",s1.marks);

    strcpy(s2.name,"priya ");
    s2.roll_no=102;
    s2.marks=90.0;

    printf("\nStudent 2 details:\n");
    printf("Name: %s\n",s2.name);   
    printf("Roll No: %d\n",s2.roll_no);
    printf("Marks: %.2f\n",s2.marks);

    // using function to display student details
    displaystudent(s1);
    printf("\n");
    displaystudent(s2);
    
}