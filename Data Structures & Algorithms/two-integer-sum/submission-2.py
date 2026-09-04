class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        res={}
        for i in range(len(nums)+1):
            remain=target-nums[i]
            if remain in res:
                return [res[remain],i]
            res[nums[i]]=i