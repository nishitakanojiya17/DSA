#Given an integer array nums, for each element nums[i], find how many numbers in the array are smaller than it.

class solution:
    def smallernumber(self,num):
        ans=[]
        for i in range (len(num)):
            count=0
            for j in range(len(num)):
                if num[j]<num[i]:
                    count +=1
            ans.append(count)
        return ans
    

obj = solution()
print(obj.smallernumber([8,1,2,2,3]))  # Output: [4,0,1,1,3] (The numbers smaller than 8 are 1, 2, 2, and 3; the numbers smaller than 1 are none; the numbers smaller than 2 are 1; the numbers smaller than 2 are 1; the numbers smaller than 3 are 1, 2, and 2)