class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max = len(nums)
        xorr = max
        for i in range(max):
            xorr ^= i ^ nums[i]
        return xorr        