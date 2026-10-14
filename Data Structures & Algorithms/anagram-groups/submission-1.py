class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for element in strs:
            key = ''.join(sorted(element))

            if key in hm:
                hm[key].append(element)
            else:
                hm[key] = [element]

        return list(hm.values())