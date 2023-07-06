import sys

input = sys.stdin.readline

K = int(input().rstrip())
for _ in range(K):
    V, E = map(int, input().rstrip().split(' '))
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().rstrip().split(' '))
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    left = [False] * V
    right = [False] * V
    for start in range(V):
        if left[start] or right[start]:
            continue
        cur = [start]
        left[start] = True
        i = 0
        possible = True
        while len(cur) > 0:
            next_round = []
            for u in cur:
                for v in graph[u]:
                    if i % 2 == 0:
                        if left[v]:
                            possible = False
                            break
                        if not right[v]:
                            right[v] = True
                            next_round.append(v)
                    else:
                        if right[v]:
                            possible = False
                            break
                        if not left[v]:
                            left[v] = True
                            next_round.append(v)
                if not possible:
                    break
            if not possible:
                break
            cur = next_round
            i += 1
        if not possible:
            break
    if possible:
        print("YES")
    else:
        print("NO")

# 교훈 단절 그래프인지 확인할 때 visited 체크를 항상 처음부터 할 필요 없이 이미 체크한 것은 넘어갈 수 있게 짜야 한다.
