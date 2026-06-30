# Write a program to display sum 1 to n ( given number). 
n=int(input("enter a no "))
sum=0
avg=0
for i in range(1,n+1):
    sum += i
    print(sum,end=" ")
    avg=sum/2
    print(avg,end="\n ")