n = int(input("Enter the array size: "))

arr = []

print("Enter the array elements:")

for i in range(n):
    element = int(input())
    arr.append(element)

print("Array elements are:")

for i in arr:
    print(i, end=" ")