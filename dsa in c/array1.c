// Program to input and print all elements of an array

#include<stdio.h>

int main()
{
    int arr[100], i, n;

    printf("Enter size of array: ");
    scanf("%d", &n);

    // Input array elements
    printf("Enter %d elements of the array:\n", n);
    for(i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    // Print array elements
    printf("Elements of the array are:\n");
    for(i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}