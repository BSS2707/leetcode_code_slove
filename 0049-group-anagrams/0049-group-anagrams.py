from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for word in strs:
            # Use sorted word as the key
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        return list(anagrams.values())
# Driver code (LeetCode handles this internally)
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
