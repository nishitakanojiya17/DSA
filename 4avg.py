#Average of Elements

arr = list(map(int, input("Enter array elements: ").split()))

#total = sum(arr)
#avg = total / len(arr)

sum=0
avg=0

for i in arr:
    sum+=i
    avg=sum/len(arr)
print("Sum of elements:", sum)
print("Average:", avg)