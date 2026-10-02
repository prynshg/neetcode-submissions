class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0
        l,r = 0, len(heights)-1
        while l<r:
            area= (r-l)* min(heights[l],heights[r])
            if heights[l]<heights[r]:
                maxarea=max(maxarea,area)
                l+=1
            elif heights[r]<heights[l]:
                maxarea=max(maxarea,area)
                r-=1
            else:
                maxarea=max(maxarea,area)
                l+=1
                r-=1
        return maxarea