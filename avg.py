#Average of Elements

arr = list(map(int, input("Enter array elements: ").split()))

total = sum(arr)
avg = total / len(arr)

print("Average:", avg)