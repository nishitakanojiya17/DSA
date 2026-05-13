arr = list(map(int, input("Enter array elements: ").split()))

count = 0
for i in arr:
    if i <0:
        count += 1

print("Count of negative numbers:", count)