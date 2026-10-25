class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for element in nums:
            res ^= element

        return res
            
        