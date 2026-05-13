# Write a program to find the maximum element in an array. 
arr = list(map(int, input("Enter array elements: ").split()))
max_element = arr[0]

for i in arr:
    if i >max_element:
        max_element =i
print("Maximum element:", max_element)