class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}
        for element in s:
            if element in hm1:
                hm1[element] += 1
            else:
                hm1[element] = 1
            
        for element in t:
            if element in hm2:
                hm2[element] += 1
            else:
                hm2[element] = 1

        if hm1 == hm2:
            return True
        else:
            return False
        