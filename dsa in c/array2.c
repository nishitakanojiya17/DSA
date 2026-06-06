//Write a program to find the sum of all elements in an array. 

#include<stdio.h>

int main()
{
    int arr[100],i,n;
    int sum=0;
    printf("Enter size of array: ");
    scanf("%d", &n);

    // Input array elements
    printf("Enter %d elements of the array:\n", n);
    for (i=0;i<n;i++)
    {
        scanf("%d", &arr[i]);

    }
    // Calculate sum of array elements
    for (i=0;i<n;i++)
    {
        sum +=arr[i];

    }
    // Print the sum of array elements
    printf("Sum of all elements in the array is: %d", sum);
}