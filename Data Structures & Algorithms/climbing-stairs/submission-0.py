class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def fibStairs(n):
            if n <= 1:
                return 1

            if n in memo:
                return memo[n] 

            memo[n] = fibStairs(n-1) + fibStairs(n-2)
            return memo[n]
        return fibStairs(n)
        
        
        