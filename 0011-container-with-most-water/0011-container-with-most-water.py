class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)

            # Move the pointer of the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Example usage
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(s.maxArea([1,1]))                # Output: 1
