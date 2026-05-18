# Input array
arr = list(map(int, input("Enter elements: ").split()))

n = len(arr)

# Reverse without using extra array
for i in range(n // 2):
    # swapping logic arr[i] → element from start
    # arr[n-i-1] → element from end
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

print("Reversed array:", arr)