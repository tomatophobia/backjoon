import sys

sys.stdin = open('input.txt', 'r')


class Belt:
    def __init__(self, idx, head, tail):
        self.idx = idx
        self.head = head
        self.tail = tail
        self.size = 0

    def push(self, present):
        if self.size == 0:
            self.head = present
            self.tail = present
        else:
            self.tail.next = present
            present.prev = self.tail
            self.tail = present
        self.size += 1

    def pushLeft(self, present):
        if self.size == 0:
            self.head = present
            self.tail = present
        else:
            self.head.prev = present
            present.next = self.head
            self.head = present
        self.size += 1

    def popLeft(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            sh = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return sh
        else:
            sh = self.head
            self.head = self.head.next
            self.head.prev = None
            sh.next = None
            self.size -= 1
            return sh

    def push_belt_to_head(self, belt):
        if belt.size == 0:
            pass
        elif self.size == 0:
            self.head = belt.head
            self.tail = belt.tail
        else:
            belt.tail.next = self.head
            self.head.prev = belt.tail
            self.head = belt.head
        self.size = self.size + belt.size

    def exchange_head(self, belt):
        if self.size == 0 and belt.size == 0:
            pass
        elif self.size == 0:
            self.pushLeft(belt.popLeft())
        elif belt.size == 0:
            belt.pushLeft(self.popLeft())
        else:
            sh = self.popLeft()
            bh = belt.popLeft()
            self.pushLeft(bh)
            belt.pushLeft(sh)

    def divide(self):
        if self.size < 2:
            return [Belt(self.idx, None, None), self]
        h1_belt = Belt(self.idx, self.head, None)
        h1_belt.size = self.size // 2
        h1_tail = self.head
        for _ in range(h1_belt.size - 1):
            h1_tail = h1_tail.next
        h1_belt.tail = h1_tail
        self.head = h1_tail.next

        h1_belt.tail.next = None
        self.head.prev = None
        self.size = self.size - h1_belt.size
        return [h1_belt, self]

    def print(self):
        # from head
        print(self.idx, end=" : ")
        sh = self.head
        for _ in range(self.size):
            print(sh.idx, end=" ")
            sh = sh.next
        print()
        # from tail
        print(self.idx, end=" : ")
        st = self.tail
        for _ in range(self.size):
            print(st.idx, end=" ")
            st = st.prev
        print()


class Present:
    def __init__(self, idx, prev, next):
        self.idx = idx
        self.prev = prev
        self.next = next


N = 0
M = 0
belts = []
presents = []

Q = int(input())
for _ in range(Q):
    # print("belt::")
    # for b in belts:
    #     b.print()
    cmd = input().rstrip().split(' ')
    # print(cmd)
    if cmd[0] == '100':
        N, M = int(cmd[1]), int(cmd[2])
        belts = [Belt(i, None, None) for i in range(N + 1)]
        presents.append(Present(-1, None, None))  # dummy
        for m in range(M):
            pidx = m + 1
            present = Present(pidx, None, None)
            presents.append(present)
            bidx = int(cmd[3 + m])
            belts[bidx].push(present)
    elif cmd[0] == '200':
        m_src, m_dst = int(cmd[1]), int(cmd[2])
        src_belt = belts[m_src]
        dst_belt = belts[m_dst]
        dst_belt.push_belt_to_head(src_belt)
        belts[m_src] = Belt(m_src, None, None)
        print(dst_belt.size)
    elif cmd[0] == '300':
        m_src, m_dst = int(cmd[1]), int(cmd[2])
        src_belt = belts[m_src]
        dst_belt = belts[m_dst]
        dst_belt.exchange_head(src_belt)
        print(dst_belt.size)
    elif cmd[0] == '400':
        m_src, m_dst = int(cmd[1]), int(cmd[2])
        src_belt = belts[m_src]
        dst_belt = belts[m_dst]

        h1_belt, h2_belt = src_belt.divide()
        dst_belt.push_belt_to_head(h1_belt)
        belts[m_src] = h2_belt
        print(dst_belt.size)
        pass
    elif cmd[0] == '500':
        p_num = int(cmd[1])
        pp = presents[p_num]
        a = -1 if pp.prev is None else pp.prev.idx
        b = -1 if pp.next is None else pp.next.idx
        print(a + 2 * b)
    elif cmd[0] == '600':
        b_num = int(cmd[1])
        bb = belts[b_num]
        a = -1 if bb.size == 0 else bb.head.idx
        b = -1 if bb.size == 0 else bb.tail.idx
        c = bb.size
        print(a + 2 * b + 3 * c)

# 잘한 점. 문제 풀기 전에 명령별로 시간 복잡도 고민하고 링크드 리스트 생각해낸 점. 반으로 나누기는 결국 해결 못했지만 일단 구현해본 점 (다행히 반으로 나누기는 그냥 O(N)으로 해도 괜찮았다.)
# 못한 점. 링크드 리스트 구현하는데 괜히 push, pop 안하고 뻐기다가 이상한 실수 많이 한 점. 선인들의 지혜를 거스르지 마라.
