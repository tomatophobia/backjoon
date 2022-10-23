import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().rstrip().split())

weight = [[] for _ in range(V + 1)]

K = int(input())

for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    weight[u].append((v, w))

spath = [float('inf')] * (V + 1)
spath[K] = 0

heap = []
heapq.heappush(heap, (0, K))

while len(heap) > 0:
    min_len, min_v = heapq.heappop(heap)

    if spath[min_v] < min_len:
        continue

    for v, w in weight[min_v]:
        if spath[v] > min_len + w:
            spath[v] = min_len + w
            heapq.heappush(heap, (spath[v], v))

for v in range(1, V + 1):
    if spath[v] == float('inf'):
        print('INF')
    else:
        print(spath[v])
