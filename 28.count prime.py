arr = list(map(int, input("Enter array: ").split()))

prime = 0
non_prime = 0

for num in arr:
    if num > 1:
        is_prime = 1
        for i in range(2, num):
            if num % i == 0:
                is_prime = 0
                break
        if is_prime == 1:
            prime += 1
        else:
            non_prime += 1
    else:
        non_prime += 1

print("Prime:", prime)
print("Non-Prime:", non_prime)