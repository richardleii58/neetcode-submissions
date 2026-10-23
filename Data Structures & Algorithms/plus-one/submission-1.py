class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        current = digits[-1] + 1
        i = 1

        while current == 10:
            digits[len(digits) - i] = 0

            if i == len(digits):
                return [1] + digits

            i += 1
            current = digits[len(digits) - i] + 1

        digits[len(digits) - i] = current
        return digits

            
