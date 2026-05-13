#. Write a program to take array elements from the user, add 5 to each element, store the results in a new array, and display the new array. 

arr=list(map(int, input("Enter array elements: ").split()))

new_arr=[]

for i in arr:
    new_arr.append(i+5)

print("Array elements after adding 5:", new_arr)