 # Write a program to count how many odd numbers are present in an array.
arr = list(map(int, input("Enter array elements: ").split()))

count = 0
for i in arr:
    if i % 2 != 0:
        count += 1

print("Count of odd numbers:", count)