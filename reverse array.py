 #Write a program to display the array elements in reverse order

arr = list(map(int, input("Enter array elements: ").split()))
print("Array elements in reverse order: ")
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")