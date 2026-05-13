# Write a program to input elements into an array and divide them into two separate arrays — one containing positive numbers and the other containing negative numbers.

arr= list(map(int, input("Enter array elements: ").split()))

pos_arr=[]
neg_arr=[]

for i in arr:
    if i >=0:
        pos_arr.append(i)
    else:
        neg_arr.append(i)

print("positive array elements are :",pos_arr)
print("negative array elements are :",neg_arr)