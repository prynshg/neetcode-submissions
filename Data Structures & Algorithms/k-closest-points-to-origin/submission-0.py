class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]

        for point in points:
            x,y=point
            distance=x*x+y*y

            heapq.heappush(heap,(-distance,point))

            if len(heap)>k:
                heapq.heappop(heap)

        result=[]
        for distance, point in heap:
            result.append(point)

        return result