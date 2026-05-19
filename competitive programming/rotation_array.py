# rotate the array by 1 to the right 

def rotate_array(arr):
    n=len(arr)

    last=arr[n-1]  #store last element

    for i in range(n-1,0,-1):
        arr[i]=arr[i-1] #shift element
    arr[0]=last #put last element at first position
    return arr

arr=[1,2,3,4,5]
result=rotate_array(arr)

print("rotated array: ", result)