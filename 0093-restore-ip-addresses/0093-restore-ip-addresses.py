class Solution:
    def restoreIpAddresses(self, s):
        ans = []

        def dfs(i, parts):
            if len(parts) == 4:
                if i == len(s):
                    ans.append(".".join(parts))
                return

            remaining = len(s) - i
            needed = 4 - len(parts)

            if remaining < needed or remaining > needed * 3:
                return

            for j in range(i, min(i + 3, len(s))):
                part = s[i:j + 1]

                if len(part) > 1 and part[0] == '0':
                    break

                if int(part) <= 255:
                    dfs(j + 1, parts + [part])

        dfs(0, [])
        return ans
