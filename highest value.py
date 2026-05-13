# Write a  program that accepts some integers from the user and finds the highest value and the input position.

arr = list(map(int, input("Enter array elements: ").split()))
max_element = arr[0]
position=0

for i in range(len(arr)):
    if arr[i]>max_element:
        max_element=arr[i]
        position=i

print("Highest value:", max_element)
print("Position of highest value:", position)