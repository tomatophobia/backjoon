import sys

sys.stdin = open('input.txt', 'r')


class Belt:
    def __init__(self, idx):
        self.idx = idx
        self.working = True
        # dummy head, tail
        self.head = Node(idx, 0, -1, None, None)
        self.tail = Node(idx, 0, -1, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, node):
        tp = self.tail.prev
        tp.next = node
        node.prev = tp
        self.tail.prev = node
        node.next = self.tail

    def popLeft(self):
        if self.head.next.weight == 0:
            return None
        hn = self.head.next
        hnn = self.head.next.next
        self.head.next = hnn
        hnn.prev = self.head
        hn.next = None
        hn.prev = None
        return hn

    def swap(self, node):
        if node.prev.weight == 0:
            return
        np = node.prev
        hn = self.head.next
        tp = self.tail.prev

        self.head.next = node
        hn.prev = tp
        np.next = self.tail
        node.prev = self.head
        tp.next = hn
        self.tail.prev = np

    def push_belt(self, belt):
        if belt.head.next.weight == 0:
            return
        tp = self.tail.prev
        bhn = belt.head.next
        btp = belt.tail.prev

        tp.next = bhn
        self.tail.prev = btp
        belt.head.next = belt.tail
        bhn.prev = tp
        btp.next = self.tail
        belt.tail.prev = belt.head


class Node:
    def __init__(self, idx, weight, idx2, prev, next):
        self.idx = idx
        self.weight = weight
        self.idx2 = idx2
        self.prev = prev
        self.next = next


Q = int(input().rstrip())
N = 0
M = 0
K = 0
belts = []
nodes = {}
belt_num = []
for _ in range(Q):
    cmd = list(map(int, input().rstrip().split(' ')))
    if cmd[0] == 100:
        N, M = cmd[1], cmd[2]
        K = N // M
        belts = [Belt(i) for i in range(M + 1)]  # 0번 벨트는 더미
        belt_num = [i for i in range(M + 1)]  # 벨트 번호 리스트: idx = node.idx2 // K + 1
        for n in range(N):
            node = Node(cmd[3 + n], cmd[3 + n + N], n, None, None)
            nodes[cmd[3 + n]] = node
            belts[n // K + 1].push(node)
    elif cmd[0] == 200:
        w_max = cmd[1]
        total = 0
        for bb in range(1, M + 1):
            check = belts[bb].popLeft()
            if check is None:
                continue
            if check.weight <= w_max:
                total += check.weight
            else:
                belts[bb].push(check)
        print(total)
    elif cmd[0] == 300:
        r_id = cmd[1]
        node = nodes.get(r_id)  # O(logN)
        if node is None or node.prev is None or node.next is None:
            print(-1)
            continue
        np = node.prev
        nn = node.next
        np.next = nn
        nn.prev = np
        node.prev = None
        node.next = None
        print(r_id)
    elif cmd[0] == 400:
        f_id = cmd[1]
        node = nodes.get(f_id)  # O(logN)
        if node is None or node.prev is None or node.next is None:
            print(-1)
            continue
        belt_id = belt_num[node.idx2 // K + 1]
        belts[belt_id].swap(node)
        print(belt_id)
    elif cmd[0] == 500:
        b_num = cmd[1]
        if not belts[b_num].working:
            print(-1)
            continue
        dst_bnum = b_num % M + 1
        while not belts[dst_bnum].working:
            dst_bnum = dst_bnum % M + 1
        belts[dst_bnum].push_belt(belts[b_num])
        belts[b_num].working = False
        for bb in range(1, M + 1):
            if belt_num[bb] == b_num:
                belt_num[bb] = dst_bnum
        print(b_num)
