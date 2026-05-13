# Write a program to input elements into an array and divide them into two separate arrays — one containing even numbers and the other containing odd numbers.

arr = list(map(int, input("Enter array elements: ").split()))
even_arr=[]
odd_arr=[]

for i in arr:
    if i%2==0:
        even_arr.append(i)
    else:
        odd_arr.append(i)
print("Even numbers are : ",even_arr)
print("Odd numbers are : ",odd_arr)