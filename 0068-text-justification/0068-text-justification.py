class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        n = len(words)
        i = 0

        while i < n:
            # Find words that fit in current line
            j = i
            line_len = 0

            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            num_words = j - i
            spaces_needed = maxWidth - line_len

            # Last line or single word -> left justify
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                gaps = num_words - 1
                even_spaces = spaces_needed // gaps
                extra_spaces = spaces_needed % gaps

                line = ""

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (
                        even_spaces + (1 if k - i < extra_spaces else 0)
                    )

                line += words[j - 1]

            res.append(line)
            i = j

        return res