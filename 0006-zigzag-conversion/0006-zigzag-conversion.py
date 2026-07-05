class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row, going_down = 0, False

        for c in s:
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        return "".join(rows)
s = Solution()
print(s.convert("PAYPALISHIRING", 3))  # Output: PAHNAPLSIIGYIR
print(s.convert("PAYPALISHIRING", 4))  # Output: PINALSIGYAHRPI
print(s.convert("A", 1))               # Output: A
