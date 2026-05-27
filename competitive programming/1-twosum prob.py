#find two no in an array whose su equals to a given target

def two_sum(arr, target):
    n=len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
               # return (i, j) # return the index of the pair
                return(arr[i],arr[j]) #retrun the no the digit of the pair 
    return None
arr=[2, 7, 11, 15]
target=9
result=two_sum(arr,target)

if result:
    print("pair found: ", result)
else:
    print("no pair found")