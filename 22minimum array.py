# Write a program to find the minimum element in an array.
arr = list(map(int, input("Enter array elements: ").split()))
min_element=arr[0]

for i in arr:
    if i<min_element:
        min_element=i
print("Minimum element:", min_element)