arr = list(map(int, input("Enter array elements: ").split()))

armstrong = 0
non_armstrong = 0

for num in arr:
    temp = num
    digits = len(str(num))
    sum = 0

    if num > 0:
        while temp > 0:
            digit = temp % 10
            sum = sum + (digit ** digits)
            temp = temp // 10

        if sum == num:
            armstrong += 1
        else:
            non_armstrong += 1
    else:
        non_armstrong += 1

print("Armstrong:", armstrong)
print("Non-Armstrong:", non_armstrong)