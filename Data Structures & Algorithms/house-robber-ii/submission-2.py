class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(i, nums, memo):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            skip = dfs(i + 1, nums, memo)
            rob = nums[i] + dfs(i + 2, nums, memo)

            temp = max(skip, rob)
            memo[i] = temp

            return memo[i]

        memo1 = {}
        memo2 = {}

        result1 = dfs(0, nums[:-1], memo1)
        result2 = dfs(0, nums[1:], memo2)

        return max(result1, result2)