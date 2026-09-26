class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)

        heap=[]
        for num, freq in count.items():
            heapq.heappush(heap,(freq,num))

            if len(heap)>k:
                heapq.heappop(heap)

        result=[]
        for freq, num in heap:
            result.append(num)

        return result