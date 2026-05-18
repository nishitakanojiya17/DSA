#. Write a program to count how many elements in an array are perfect and how many are not perfect.
arr = list(map(int, input("Enter array elements: ").split()))

perfect = 0
non_perfect = 0

for num in arr:
    sum = 0

    if num > 0:
        for i in range(1, num):
            if num % i == 0:
                sum = sum + i

        if sum == num:
            perfect = perfect + 1
        else:
            non_perfect = non_perfect + 1
    else:
        non_perfect = non_perfect + 1

print("Perfect numbers:", perfect)
print("Non-Perfect numbers:", non_perfect)