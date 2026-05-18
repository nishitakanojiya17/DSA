#Sum + Check Even or Odd
arr = list(map(int, input("Enter array elements: ").split()))
#total = sum(arr)
sum=0

for i in arr:
    sum+=i
print("Sum of elements:", sum)
if sum % 2 == 0:
    print("Sum is Even")
else:
    print("Sum is Odd")




