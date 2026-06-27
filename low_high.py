#Given two non-negative integers low and high, return the count of odd numbers between low and high (inclusive).

class Solution:
    def countOdds(self, low: int, high: int) -> int:

        count = 0

        for i in range(low, high + 1):
            if i % 2 != 0:
                count += 1

        return count
    
obj= Solution()
print(obj.countOdds(3,10))  # Output: 3 (The odd numbers between 3 and 7 are 3, 5, and 7)