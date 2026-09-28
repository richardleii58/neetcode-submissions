class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        def anagram(s, t):
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
        res = []
        for i in range(len(strs)):
            resin = []
            for z in range(len(strs)):
                if (len(strs[z]) == len(strs[i])):
                    if anagram(strs[z], strs[i]):
                        resin.append(strs[z])     

            if resin not in res:
                res.append(resin) 
            


        return res


            