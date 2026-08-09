class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # index for placing non-val elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# 🔎 Demo usage
if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = s.removeElement(nums1, val1)
    print("Example 1:")
    print("k =", k1)              # Expected: 2
    print("nums =", nums1[:k1])   # Expected: [2, 2]

    # Example 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = s.removeElement(nums2, val2)
    print("\nExample 2:")
    print("k =", k2)              # Expected: 5
    print("nums =", nums2[:k2])   # Expected: [0, 1, 3, 0, 4] (order may vary)
