class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        k -= 1
        result = []
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            j = k // f
            result.append(nums.pop(j))
            k %= f
        return ''.join(result)