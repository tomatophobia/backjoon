import sys
sys.stdin = open('input.txt', 'r')
from time import time

import heapq

Q = int(input())
grader = []
domain_status = {}  # domain -> [채점 중, 쿨타임, 대기 큐]
url_status = {}  # url -> [대기 중]
N = 0

for _ in range(Q):
    cmd = input().rstrip().split()
    # print(waiting_queue)
    # print(grader)
    # print(domain_status)
    # print(url_status)
    # print("---")
    # print(cmd)
    if cmd[0] == '100':
        N, u0 = int(cmd[1]), cmd[2]
        grader = [[] for _ in range(N + 1)]
        domain, pid = u0.split('/')
        pid = int(pid)
        url_status[u0] = [True]
        domain_status[domain] = [False, 0, [[1, 0, pid]]]
    elif cmd[0] == '200':
        t, p, u = int(cmd[1]), int(cmd[2]), cmd[3]
        domain, pid = u.split('/')
        pid = int(pid)
        us = url_status.get(u)  # log(50000)
        if us is None:
            url_status[u] = [True]
        elif us[0]:
            continue
        else:
            us[0] = True
        ds = domain_status.get(domain)
        if ds is None:
            domain_status[domain] = [False, 0, [[p, t, pid]]]
        else:
            heapq.heappush(ds[2], [p, t, pid])
    elif cmd[0] == '300':
        t = int(cmd[1])
        rest_grader = -1
        for n in range(1, N + 1):  # 50000 -> 근데 직접 프린트 해보면 거의 ~100
            if len(grader[n]) == 0:
                rest_grader = n
                break
        if rest_grader == -1:
            continue
        best_ds = None
        best_domain = None
        for domain, ds in domain_status.items():
            if ds[0] or t < ds[1] or len(ds[2]) == 0:
                continue
            if best_ds is None or ds[2][0] < best_ds[2][0]:
                best_ds = ds
                best_domain = domain
        if best_ds is None:
            continue
        best_ds[0] = True
        _, _, pid = heapq.heappop(best_ds[2])
        url_status[best_domain + "/" + str(pid)] = [False]
        grader[rest_grader].append([t, best_domain, pid])
    elif cmd[0] == '400':
        t, jid = int(cmd[1]), int(cmd[2])
        if len(grader[jid]) == 0:
            continue
        s, domain, pid = grader[jid].pop()
        ds = domain_status[domain]
        ds[0] = False
        ds[1] = s + 3 * (t - s)
    elif cmd[0] == '500':
        t = int(cmd[1])
        count = 0
        for _, ds in domain_status.items():
            count += len(ds[2])
        print(count)
