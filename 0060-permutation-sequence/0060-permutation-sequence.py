class Solution:
    def getPermutation(self, n, k):
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1

        result = []
        for i in range(n - 1, -1, -1):
            idx = k // fact[i]
            result.append(numbers.pop(idx))
            k %= fact[i]

        return "".join(result)