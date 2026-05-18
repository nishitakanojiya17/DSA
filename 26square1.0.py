# Write a program to take array elements from the user, store their squares in a new array, and display the new array.


arr=list(map(int,input("enter the array elements : ").split()))
sq_arr=[]

for i in arr:
    sq_arr.append(i**2)

print("square of the array elements are : ",sq_arr)