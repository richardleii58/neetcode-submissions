class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        #count = len(output)
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if j == i:
                    pass
                else:
                    temp *= nums[j]

            output.append(temp)

        return output

                
            
        