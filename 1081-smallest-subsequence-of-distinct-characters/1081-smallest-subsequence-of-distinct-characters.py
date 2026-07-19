class Solution:
    def smallestSubsequence(self, s):
        from collections import Counter
        
        freq = Counter(s)
        stack = []
        visited = set()
        
        for ch in s:
            freq[ch] -= 1
            if ch in visited:
                continue
            while stack and ch < stack[-1] and freq[stack[-1]] > 0:
                visited.remove(stack.pop())
            stack.append(ch)
            visited.add(ch)
        
        return "".join(stack)
