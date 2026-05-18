#Display Positive Numbers
arr = list(map(int, input("Enter array elements: ").split()))
print("positive no are : ")
for i in arr:
    if i>=0:
        print(i,end="")