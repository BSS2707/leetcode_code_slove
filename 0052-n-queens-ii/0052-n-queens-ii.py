class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        cols = set()   # columns with queens
        diag1 = set()  # r - c diagonals
        diag2 = set()  # r + c diagonals

        def backtrack(r):
            if r == n:
                self.count += 1
                return
            
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                
                backtrack(r + 1)
                
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return self.count
sol = Solution()
print(sol.totalNQueens(4))  # Output: 2
print(sol.totalNQueens(1))  # Output: 1
