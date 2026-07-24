class Solution:
    def intToRoman(self, num):
        val = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4,
               1]
        syms = ["M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"]
        
        roman = ""
        i = 0
        while num > 0:
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]
            i += 1
        return roman

# Demo
s = Solution()
print(s.intToRoman(3749))  # MMMDCCXLIX
print(s.intToRoman(58))    # LVIII
print(s.intToRoman(1994))  # MCMXCIV
