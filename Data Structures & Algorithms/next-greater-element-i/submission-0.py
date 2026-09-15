class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        freq={}
        for x in nums2:
            while stack and x>stack[-1]:
                pop=stack.pop()
                freq[pop]=x
            stack.append(x)
        while stack:
            freq[stack.pop()]=-1
        return [freq[i] for i in nums1]