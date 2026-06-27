#Given an integer num, return the number of digits in num that divide num completely.

class solution:
    def dividecomplete(self,num):
        count=0
        for i in str(num):
            if i !=0 and num % int(i)==0:
                count+=1
        return count
obj=solution()
print(obj.dividecomplete(1211))  