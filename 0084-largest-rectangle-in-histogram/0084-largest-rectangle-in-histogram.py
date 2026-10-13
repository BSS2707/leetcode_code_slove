class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):
            curr_height = 0 if i == len(heights) else heights[i]

            while stack and heights[stack[-1]] > curr_height:
                h = heights[stack.pop()]

                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i

                max_area = max(max_area, h * w)

            stack.append(i)

        return max_area