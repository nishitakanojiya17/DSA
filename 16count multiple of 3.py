arr = list(map(int, input("Enter array elements: ").split()))
count = 0

for i in arr:
    if i % 3 == 0:
        count += 1

print("Count multiples of 3:", count)