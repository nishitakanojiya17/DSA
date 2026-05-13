#Sum + Check Even or Odd
arr = list(map(int, input("Enter array elements: ").split()))
total = sum(arr)

print("Sum:", total)

if total % 2 == 0:
    print("Sum is Even")
else:
    print("Sum is Odd")
