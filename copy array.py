# Write a program to copy elements from one array to another. 
arr = list(map(int, input("Enter array elements: ").split()))
copy_arr = []

for i in arr:
    copy_arr.append(i)

print("Copied array:", copy_arr)

