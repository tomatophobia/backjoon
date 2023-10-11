import sys

sys.stdin = open('input.txt', 'r')


class Belt:
    def __init__(self, num):
        self.num = num
        self.size = 0
        self.head = Box(-num)
        self.tail = Box(-num)
        self.head.next = self.tail
        self.head.prev = None
        self.tail.prev = self.head
        self.tail.next = None

    def push(self, box):
        tp = self.tail.prev
        tp.next = box
        box.prev = tp
        box.next = self.tail
        self.tail.prev = box
        self.size += 1

    def pushleft(self, box):
        hn = self.head.next
        box.next = hn
        hn.prev = box
        self.head.next = box
        box.prev = self.head
        self.size += 1

    def popleft(self):
        if self.size == 0:
            return None
        hn = self.head.next
        hnn = self.head.next.next
        self.head.next = hnn
        hnn.prev = self.head
        hn.next = None
        hn.prev = None
        self.size -= 1
        return hn

    def pushleftall(self, belt):
        if belt.size == 0:
            return

        bhn = belt.head.next
        btp = belt.tail.prev
        hn = self.head.next

        self.head.next = bhn
        bhn.prev = self.head
        btp.next = hn
        hn.prev = btp

        belt.head.next = belt.tail
        belt.tail.prev = belt.head

        self.size += belt.size
        belt.size = 0

    def take_half(self, belt):
        if belt.size // 2 == 0:
            return
        bhn = belt.head.next
        bhh = belt.head
        for _ in range(belt.size // 2):
            bhh = bhh.next
        bhhn = bhh.next

        hn = self.head.next

        self.head.next = bhn
        bhn.prev = self.head
        bhh.next = hn
        hn.prev = bhh

        belt.head.next = bhhn
        bhhn.prev = belt.head

        self.size += belt.size // 2
        belt.size -= belt.size // 2

    def print(self):
        hn = self.head.next
        while hn.num > 0:
            print(hn.num, end=' ')
            hn = hn.next
        print('')
        tp = self.tail.prev
        bstr = ''
        while tp.num > 0:
            bstr = str(tp.num) + ' ' + bstr
            tp = tp.prev
        print(bstr)


class Box:
    def __init__(self, num):
        self.num = num
        self.prev = None
        self.next = None


Q = int(input().rstrip())
N, M = 0, 0
belts = []
boxes = [None]  # 0번은 더미
for _ in range(Q):
    cmd = list(map(int, input().rstrip().split(' ')))
    if cmd[0] == 100:
        N, M = cmd[1], cmd[2]
        belts = [Belt(i) for i in range(0, N + 1)]  # 0번은 더미
        for i in range(M):
            box = Box(i + 1)
            boxes.append(box)
            belt_num = cmd[3 + i]
            belts[belt_num].push(box)
    elif cmd[0] == 200:
        m_src, m_dst = cmd[1], cmd[2]
        belt_dst = belts[m_dst]
        belt_src = belts[m_src]
        belt_dst.pushleftall(belt_src)
        print(belt_dst.size)
    elif cmd[0] == 300:
        m_src, m_dst = cmd[1], cmd[2]
        belt_dst = belts[m_dst]
        belt_src = belts[m_src]

        dst_box = belt_dst.popleft()
        src_box = belt_src.popleft()
        if dst_box is not None:
            belt_src.pushleft(dst_box)
        if src_box is not None:
            belt_dst.pushleft(src_box)
        print(belt_dst.size)
    elif cmd[0] == 400:
        m_src, m_dst = cmd[1], cmd[2]
        belt_dst = belts[m_dst]
        belt_src = belts[m_src]
        belt_dst.take_half(belt_src)
        print(belt_dst.size)
    elif cmd[0] == 500:
        p_num = cmd[1]
        box = boxes[p_num]
        a = box.prev.num if box.prev.num > 0 else -1
        b = box.next.num if box.next.num > 0 else -1
        print(a + 2 * b)
    elif cmd[0] == 600:
        b_num = cmd[1]
        belt = belts[b_num]
        a = belt.head.next.num if belt.head.next.num > 0 else -1
        b = belt.tail.prev.num if belt.tail.prev.num > 0 else -1
        c = belt.size
        print(a + 2 * b + 3 * c)
