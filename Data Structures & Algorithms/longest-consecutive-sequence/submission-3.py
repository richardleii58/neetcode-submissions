class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        res = 1
        mx = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                mx += 1
            elif nums[i] != nums[i+1]:  
                res = max(res, mx)
                mx = 1
        return max(res, mx)
