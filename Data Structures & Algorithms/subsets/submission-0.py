import math
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = [[]]

        for num in nums:
            for subset in final[:]:
                new_subset = subset + [num]
                final.append(new_subset)

        return final




        