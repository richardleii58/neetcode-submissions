class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] = 1
        
        res = []
        dic = dict(sorted(dic.items(), key=lambda item: item[1]))
        keys = list(dic.keys())
        print(keys)
        for i in range(k):
            res.append(keys[-i-1])

        return res
        