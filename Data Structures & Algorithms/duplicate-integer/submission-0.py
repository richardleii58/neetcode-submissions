class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for element in nums:
            if element in hm:
                return True
            else:
                hm[element] = 1

        return False