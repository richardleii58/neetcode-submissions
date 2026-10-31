
class Solution:
    def to_twos_complement(self, n):
        bits = list(format(abs(n), "032b"))

        if n >= 0:
            return int("".join(bits), 2)

        # Invert all bits
        bits = ["1" if bit == "0" else "0" for bit in bits]

        # Add 1 using XOR and carry
        carry = 1
        for i in reversed(range(32)):
            bit = int(bits[i])
            bits[i] = str(bit ^ carry)
            carry = bit & carry

        return int("".join(bits), 2)

    def to_signed(self, n):
        bits = format(n, "b").zfill(32)[-32:]

        if bits[0] == "0":
            return int(bits, 2)

        # Invert bits and interpret as negative
        flipped = "".join(
            "1" if bit == "0" else "0" for bit in bits
        )
        return ~int(flipped, 2)

    def getSum(self, a: int, b: int) -> int:
        a = self.to_twos_complement(a)
        b = self.to_twos_complement(b)

        result = 0
        carry = 0
        position = 0

        while a or b or carry:
            bit1 = a & 1
            bit2 = b & 1

            current_bit = bit1 ^ bit2 ^ carry
            new_carry = (bit1 & bit2) | (bit1 & carry) | (bit2 & carry)

            result |= current_bit << position

            a >>= 1
            b >>= 1

            carry = new_carry
            position += 1

        return self.to_signed(result)
   
        