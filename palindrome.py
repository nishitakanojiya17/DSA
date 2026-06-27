# palindrome

class solution:
    def is_palindrome(self,num):
        
        if  (str(num)==str(num)[::-1]): 
            return "No is palindrome"
        else:
            return "No is not palindrome"
        
    
    
obj=solution()
print(obj.is_palindrome(121))  # Output: True
print(obj.is_palindrome(123))  # Output: False