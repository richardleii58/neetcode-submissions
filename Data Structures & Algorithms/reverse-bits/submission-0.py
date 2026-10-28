class Solution:
    def reverseBits(self, n: int) -> int:

        c = bin(n)[2:].zfill(32)[::-1]
        res = 0
        count = 31
        for char in c:
            if char == "1":
                res += int(2 ** count)
            count -=1

        return res
   