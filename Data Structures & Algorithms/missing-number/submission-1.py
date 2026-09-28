class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result =0 
        for i, c in enumerate(nums):
            result^=i
            result^=c
        result^=len(nums)
        return result
