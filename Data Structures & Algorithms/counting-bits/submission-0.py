class Solution:
    def countBits(self, n: int) -> List[int]:

        def numBits(n):
            result = 0

            while n > 0:
                remainder = n % 2
                n = n // 2
                if remainder == 1:
                    result += 1

            return result    
        res= []
        for i in range(n+1):
            res.append(numBits(i))

        return res
