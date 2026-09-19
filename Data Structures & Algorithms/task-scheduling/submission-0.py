class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count={}
        for task in tasks:
            count[task]=1+count.get(task,0)

        heap=[]
        for task, freq in count.items():
            heapq.heappush(heap,(-freq,task))

        cooldown=[]
        time=0

        while heap or cooldown:
            time+=1

            while cooldown and cooldown[0][0]<=time:
                ready_time, remaining, task= heapq.heappop(cooldown)
                heapq.heappush(heap,(-remaining, task))

            if heap:
                freq, task=heapq.heappop(heap)
                freq+=1

                if freq<0:
                    heapq.heappush(cooldown,(time+n+1, -freq, task))

        return time                    

