#Display Numbers multiple by 3
arr = list(map(int, input("Enter array elements: ").split()))
print("multiple by 3 are : ")
for i in arr:
    if i%3==0:
        print(i,end="")