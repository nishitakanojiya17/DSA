#Display Odd Numbers
arr = list(map(int, input("Enter array elements: ").split()))
print("odd no are : ")
for i in arr:
    if i%2!=0:
        print(i,end="")