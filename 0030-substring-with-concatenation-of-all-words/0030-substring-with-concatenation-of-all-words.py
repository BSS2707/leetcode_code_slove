class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])          # length of each word
        total_len = word_len * len(words) # total length of concatenated substring
        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1

        res = []

        # Try each possible offset within word_len
        for offset in range(word_len):
            left = offset
            seen = {}
            count = 0

            # Slide window
            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right+word_len]
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    # Shrink window if word frequency exceeds
                    while seen[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # If window matches all words
                    if count == len(words):
                        res.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return res


# ✅ Example Runs
s = "barfoothefoobarman"
words = ["foo","bar"]
print(Solution().findSubstring(s, words))  # Output: [0, 9]

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(Solution().findSubstring(s, words))  # Output: []

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(Solution().findSubstring(s, words))  # Output: [6, 9, 12]
