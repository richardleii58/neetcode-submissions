class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = ""
        for i in range(len(strs)):
            temp += str(len(strs[i]))
            temp += "#"
            temp += strs[i]
      
        return temp
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        encoded = s
        while i < len(encoded):
            j = i
            while encoded[j] != '#':
                j += 1
            length = int(encoded[i:j])
            res.append(encoded[j+1:j+1+length])
            i = j + 1 + length

        return res
                
