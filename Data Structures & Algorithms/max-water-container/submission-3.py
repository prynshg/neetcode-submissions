class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0
        l,r=0,len(heights)-1
        while l<r:
            area=(r-l)*min(heights[r],heights[l])
            if heights[l]<heights[r]:
                maxArea=max(maxArea,area)
                l+=1
            elif heights[r]<heights[l]:
                maxArea=max(maxArea,area)
                r-=1
            else:
                maxArea=max(maxArea,area)
                l+=1
                r-=1
        return maxArea