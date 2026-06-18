// Structure pointer example
#include <stdio.h>
#include <stdlib.h>

struct emp
{
    int id;
    float salary;
};  

int main()
{
    struct emp e1;
    struct emp *ptr; // pointer to structure

    ptr = &e1; // pointer stores address of e1

    (*ptr).id = 101;
    (*ptr).salary = 50000;

    printf("emp id: %d\n", (*ptr).id);
    printf("emp salary: %.2f\n", (*ptr).salary);

    return 0;
}