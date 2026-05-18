#Display Numbers Divisible by 4
arr = list(map(int, input("Enter array elements: ").split()))
print("divisible by 4 are : ")
for i in arr:
    if i%4==0:
        print(i,end="")