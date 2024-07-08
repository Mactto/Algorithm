import heapq

def dijkstra(N, edges):
    graph = {i: [] for i in range(1, N+1)}

    for node1, node2, value in edges:
        graph[node1].append((value, node2))
        graph[node2].append((value, node1))

    # 최소 힙을 이용한 다익스트라 알고리즘
    heap = [(0, 1)]  # (거리, 노드) 초기 시작점은 거리 0, 노드 1
    distances = {i: float('inf') for i in range(1, N+1)}
    distances[1] = 0
    visited = [False] * (N + 1)

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if visited[current_node]:
            continue
        
        visited[current_node] = True

        for weight, neighbor in graph[current_node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances[N]

# 입력 받기
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# 다익스트라 알고리즘 실행
result = dijkstra(N, edges)
print(result)
