import heapq

def dijkstra(start, end):
    INF = int(1e9)  
    distance = [INF] * (end + 1)
    distance[start] = 0

    pq = [(0, start)]  

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        
        next_pos = now - 1
        if 0 <= next_pos <= end and distance[next_pos] > dist + 1:
            distance[next_pos] = dist + 1
            heapq.heappush(pq, (dist + 1, next_pos))

        
        next_pos = now + 1
        if 0 <= next_pos <= end and distance[next_pos] > dist + 1:
            distance[next_pos] = dist + 1
            heapq.heappush(pq, (dist + 1, next_pos))

        
        next_pos = now * 2
        if 0 <= next_pos <= end and distance[next_pos] > dist:
            distance[next_pos] = dist
            heapq.heappush(pq, (dist, next_pos))

    return distance[end]


N, K = map(int, input().split())
result = dijkstra(N, K)


print(result)