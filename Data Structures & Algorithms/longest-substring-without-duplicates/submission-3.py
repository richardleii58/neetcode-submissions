class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen ={}
        res = 0
        current = 0
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i

            else:

                current = max(seen[s[i]] + 1, current)
                seen[s[i]] = i            
            res = max(i - current + 1, res)                

        return res

        