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
  // take the input from the user for student 1
    printf("Enter details for student 1:\n");
    printf("Name: ");
    scanf("%s",s1.name);
    printf("Roll No: ");
    scanf("%d",&s1.roll_no);
    printf("Marks: ");
    scanf("%f",&s1.marks);

    printf("\nStudent 2 details:\n");
    printf("Name: ");
    scanf("%s",s2.name);
    printf("Roll No: ");
    scanf("%d",&s2.roll_no);
    printf("Marks: ");
    scanf("%f",&s2.marks);
}