# Write a program to display multiple of   7  between given range. 
# Program to display multiples of 7 between a given range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Multiples of 7 between {start} and {end}:")
for i in range(start, end+1):
    if i % 7 == 0:
        print(i, end=" ")

