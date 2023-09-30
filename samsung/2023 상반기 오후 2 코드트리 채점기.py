import sys
sys.stdin = open('input.txt', 'r')
from time import time

import heapq

Q = int(input())
grader = []
waiting_queue = []
domain_status = {}  # domain -> [채점 중, 쿨타임]
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
        domain_status[domain] = [False, 0]
        heapq.heappush(waiting_queue, (1, 0, domain, pid))
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
            domain_status[domain] = [False, 0]
        heapq.heappush(waiting_queue, (p, t, domain, pid))  # log(50000)
    elif cmd[0] == '300':
        time1 = time()
        t = int(cmd[1])
        rest_grader = -1
        for n in range(1, N + 1):  # 50000 -> 근데 직접 프린트 해보면 거의 ~100
            if len(grader[n]) == 0:
                rest_grader = n
                break
        if rest_grader == -1:
            continue
        fail = []
        time2 = time()
        while len(waiting_queue) > 0:
            element = heapq.heappop(waiting_queue)  # log(50000)
            _, _, domain, pid = element
            ds = domain_status[domain]  # log(300)
            if not ds[0] and t >= ds[1]:
                ds[0] = True
                url_status[domain + "/" + str(pid)] = [False]  # log(50000)
                grader[rest_grader].append([t, domain, pid])
                break
            fail.append(element)
        time3 = time()
        waiting_queue = waiting_queue + fail  # 실패하는 수가 많을까? ~5000 일단 보류
        heapq.heapify(waiting_queue)  # log(50000)
        time4 = time()
        print("---")
        print(f'{time2 - time1:.5f}')
        print(f'{time3 - time2:.5f}')
        print(f'{time4 - time3:.5f}')
        print(f'{time4 - time1:.5f}')
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
        # print(len(waiting_queue))
