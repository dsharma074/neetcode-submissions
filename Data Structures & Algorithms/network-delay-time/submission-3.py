class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        pq = []
        distance = [float('inf')]*(n+1)

        adjlist = [[] for _ in range(n+1)]
        for i in times:
            adjlist[i[0]].append((i[2],i[1]))
        print(adjlist)
        
        heapq.heappush(pq,(0,k))
        distance[k] = 0
        while pq:
            d, node = heapq.heappop(pq)
            for nd, nn in adjlist[node]:
                ud = nd+d
                if distance[nn] > ud:
                    distance[nn] = ud
                    heapq.heappush(pq,(ud,nn))
        print(distance)
        val = max(distance[1:])
        if val == float('inf'):
            return -1
        else:
            return val




        

        