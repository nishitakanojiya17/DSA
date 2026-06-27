class FizzBuzz:

    def __init__(self, n):
        self.n = n

    def fizzbuzz(self):
        ans = []

        for i in range(1, self.n + 1):  # n= 1 to 15 
            # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans


obj = FizzBuzz(15)
print(obj.fizzbuzz())