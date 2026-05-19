#find two no in an array whose subtraction equals to a given target

def two_sub(arr, target):
    n=len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] - arr[j] == target:
               # return (i, j) # return the index of the pair
                return(arr[i],arr[j]) #retrun the no the digit of the pair 
    return None
arr=[10, 7, 5, 2]
target=3
result=two_sub(arr,target)

if result:
    print("pair found: ", result)
else:
    print("no pair found")