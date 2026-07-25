class Solution:
    def romanToInt(self, s):
        # Mapping Roman numerals to values
        values = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        
        total = 0
        for i in range(len(s)):
            # If next symbol exists and is larger, subtract current
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total

# Demo
s = Solution()
print(s.romanToInt("III"))      # 3
print(s.romanToInt("LVIII"))    # 58
print(s.romanToInt("MCMXCIV"))  # 1994
