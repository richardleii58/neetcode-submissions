class Solution:
    def isHappy(self, n: int) -> bool:
        def square_digits(n):
            total = 0

            for digit in str(n):
                number = int(digit)
                squared = number ** 2
                total += squared

            return total

        past = {}
        while True:
            if square_digits(n) != 1:
                if square_digits(n) in past:
                    return False
                else:
                    past[n] = 1
                    n = square_digits(n)
            else:
                return True        