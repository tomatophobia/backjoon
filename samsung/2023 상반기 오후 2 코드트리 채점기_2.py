import sys

sys.stdin = open('input.txt', 'r')

import heapq

url_status = {}  # url -> 대기 중 여부
domain_status = {}  # 도메인 -> (실행 중 여부, 재가동 시간, WQ), WQ = pq of [우선순위, 대기 시작 시간, url]
judge = []  # 채점기 N개, [시작시간, url]

Q = int(input().rstrip())
for _ in range(Q):
    cmd = input().rstrip().split(' ')
    if cmd[0] == '100':
        N, u0 = int(cmd[1]), cmd[2]
        judge = [None] * (N + 1)  # 0번은 더미
        url_status[u0] = True
        domain, _ = u0.split('/')
        domain_status[domain] = [False, 0, [[1, 0, u0]]]
    elif cmd[0] == '200':
        t, p, u = int(cmd[1]), int(cmd[2]), cmd[3]
        url_is_waiting = url_status.get(u)
        if url_is_waiting is not None and url_is_waiting:
            continue
        url_status[u] = True
        domain, _ = u.split('/')
        domain_info = domain_status.get(domain)
        if domain_info is None:
            domain_status[domain] = [False, 0, [[p, t, u]]]
        else:
            heapq.heappush(domain_info[2], [p, t, u])
    elif cmd[0] == '300':
        t = int(cmd[1])
        best_info = None
        best_score = [float('inf'), float('inf')]
        for domain, info in domain_status.items():
            if info[0] or t < info[1] or len(info[2]) == 0:
                continue
            candidate = info[2][0]  # [우선순위, 대기시작시간, url]
            if candidate[:2] < best_score:
                best_score = candidate[:2]
                best_info = info
        if best_info is None:
            continue
        for jgidx in range(1, len(judge)):
            if judge[jgidx] is None:
                best_info[0] = True
                _, _, best_url = heapq.heappop(best_info[2])
                url_status[best_url] = False
                judge[jgidx] = [t, best_url]
                break
    elif cmd[0] == '400':
        t, jid = int(cmd[1]), int(cmd[2])
        if judge[jid] is None:
            continue
        start_time, url = judge[jid]
        domain, _ = url.split('/')
        domain_status[domain][0] = False
        domain_status[domain][1] = start_time + 3 * (t - start_time)
        judge[jid] = None
    elif cmd[0] == '500':
        t = int(cmd[1])
        count = 0
        for vv in domain_status.values():
            count += len(vv[2])
        print(count)
# 까먹고 break 문을 안썼다. 사소한 실수 조심하자.
# 채점기가 비어있으면 넘어갈 때 아무 일도 일어나지 않아야 하는데 미리 데이터를 뽑아서 문제가 생겼다.
# 항상 그냥 continue로 넘어갈 때 내가 미리 무슨 짓을 하지 않았는지 확인하자.
