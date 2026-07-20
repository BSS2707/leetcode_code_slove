class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total  # effective shifts

        # Flatten the grid into a 1D list
        flat = [grid[i][j] for i in range(m) for j in range(n)]

        # Perform the shift
        flat = flat[-k:] + flat[:-k]

        # Rebuild the 2D grid
        new_grid = []
        for i in range(m):
            new_grid.append(flat[i*n:(i+1)*n])

        return new_grid
s = Solution()
print(s.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1))
# Output: [[9,1,2],[3,4,5],[6,7,8]]

print(s.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4))
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

print(s.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9))
# Output: [[1,2,3],[4,5,6],[7,8,9]]
