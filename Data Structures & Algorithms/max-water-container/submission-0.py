class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        fast, slow = 0, len(heights) -1
        for i in range(len(heights)):
            temp = (slow - fast) * min(heights[fast], heights[slow])
            res = max(temp,res)
            if min(heights[fast], heights[slow]) == heights[fast]:
                fast += 1
            else:
                slow -=1

        return res        