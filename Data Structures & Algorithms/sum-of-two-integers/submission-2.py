class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF

        while b:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        # Convert 32-bit unsigned result to signed integer
        if a > 0x7FFFFFFF:
            a -= 0x100000000

        return a