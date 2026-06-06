#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#Return the answer with the smaller index first.
##Example 1:
#Input: 
#nums = [3,4,5,6], target = 7
#Output: [0,1]


class sum:
    def twosum(self,num,target):
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if num[i]+num[j]==target:
                    return [i,j]
                num[i]+num[j]
num = [3,4,5,6]
target = 7
num=[4,5,6]
target=10
s=sum()
print(s.twosum(num,target))

