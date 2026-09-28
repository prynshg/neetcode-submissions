class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        for mask in range(1<<len(nums)):
            curr=[]

            for i in range(len(nums)):
                if mask & (1<<i):
                    curr.append(nums[i])
            res.append(curr)
        return res
            