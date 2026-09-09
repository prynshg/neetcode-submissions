class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mxArea=0
        l, r= 0, len(heights)-1
        while l<r:
            mxDist=r-l
            mxArea=max(mxArea,mxDist*min(heights[l],heights[r]))
            if heights[l]<heights[r]:
                l+=1
            else :
                r-=1
        return mxArea
