import bisect

class Solution(object):
    def gcdValues(self, nums, queries):
        MAX = max(nums)

        # Step 1: Frequency of each number
        freq = [0] * (MAX + 1)
        for x in nums:
            freq[x] += 1

        # Step 2: Count how many numbers divisible by d
        cnt = [0] * (MAX + 1)
        for d in range(1, MAX + 1):
            for multiple in range(d, MAX + 1, d):
                cnt[d] += freq[multiple]

        # Step 3: Count pairs with exact gcd = d
        pairs = [0] * (MAX + 1)
        for d in range(MAX, 0, -1):
            if cnt[d] >= 2:
                pairs[d] = cnt[d] * (cnt[d] - 1) // 2
                for multiple in range(2*d, MAX + 1, d):
                    pairs[d] -= pairs[multiple]

        # Step 4: Build prefix sums (sorted by gcd value)
        gcd_values = []
        prefix = []
        total = 0
        for d in range(1, MAX + 1):
            if pairs[d] > 0:
                gcd_values.append(d)
                total += pairs[d]
                prefix.append(total)

        # Step 5: Answer queries using binary search
        answer = []
        for q in queries:
            # find smallest index where prefix >= q+1
            idx = bisect.bisect_left(prefix, q+1)
            answer.append(gcd_values[idx])
        return answer
s = Solution()
print(s.gcdValues([2,3,4], [0,2,2]))       # [1,2,2]
print(s.gcdValues([4,4,2,1], [5,3,1,0]))   # [4,2,1,1]
print(s.gcdValues([2,2], [0,0]))           # [2,2]
