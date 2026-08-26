class Solution:
    def multiply(self, num1, num2):
        # Edge case: if either number is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                sum_ = mul + res[p2]
                
                res[p1] += sum_ // 10
                res[p2] = sum_ % 10
        
        # Build result string
        result = []
        for digit in res:
            if not (len(result) == 0 and digit == 0):
                result.append(str(digit))
        
        return "".join(result)
s = Solution()
print(s.multiply("2", "3"))       # "6"
print(s.multiply("123", "456"))   # "56088"
