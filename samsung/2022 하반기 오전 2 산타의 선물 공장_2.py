import sys

sys.stdin = open('input.txt', 'r')


class Belt:
    def __init__(self, id):
        # dummy head, tail
        self.head = Box(id, 0, id)
        self.tail = Box(id, 0, id)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def push(self, box):
        tp = self.tail.prev

        tp.next = box
        box.prev = tp
        box.next = self.tail
        self.tail.prev = box

    def popleft(self):
        if self.head.next.weight == 0:
            # 벨트가 비었을 때
            return None
        hn = self.head.next
        hnn = self.head.next.next

        self.head.next = hnn
        hnn.prev = self.head
        hn.prev = None
        hn.next = None
        return hn

    def pushall(self, belt):
        if belt.head.next.weight == 0:
            # 벨트가 비었을 때
            return
        tp = self.tail.prev
        bhn = belt.head.next
        btp = belt.tail.prev

        tp.next = bhn
        bhn.prev = tp
        btp.next = self.tail
        self.tail.prev = btp

    def print(self):
        hn = self.head.next
        while hn.weight != 0:
            print(f'{hn.id}:{hn.weight}', end=' ')
            hn = hn.next
        print('')
        tp = self.tail.prev
        str = ''
        while tp.weight != 0:
            str = f'{tp.id}:{tp.weight} ' + str
            tp = tp.prev
        print(str)


class Box:
    def __init__(self, id, weight, belt_id):
        self.id = id
        self.weight = weight
        self.belt_id = belt_id
        self.prev = None
        self.next = None


Q = int(input().rstrip())
N = 0
boxes = {}
M = 0
belts = [None]  # 1번 더미
belts_pointer = []
# boxes, belts를 갱신해야 한다.
for _ in range(Q):
    cmd = list(map(int, input().rstrip().split(' ')))
    if cmd[0] == 100:
        N, M = cmd[1], cmd[2]
        for i in range(1, M + 1):
            belts.append(Belt(i))
        belts_pointer = [i for i in range(M + 1)]
        for i in range(N):
            bid, weight = cmd[3 + i], cmd[3 + N + i]
            k = N // M
            belt_id = i // k + 1
            box = Box(bid, weight, belt_id)
            boxes[bid] = box
            belts[belt_id].push(box)
    elif cmd[0] == 200:
        w_max = cmd[1]
        total = 0
        for belt in belts:
            if belt is None:
                continue
            box = belt.popleft()
            if box is None:
                continue
            if box.weight <= w_max:
                total += box.weight
                boxes[box.id] = None
            else:
                belt.push(box)
        print(total)
    elif cmd[0] == 300:
        rid = cmd[1]
        box = boxes.get(rid)
        if box is None:
            print(-1)
            continue
        boxes[rid] = None
        bp = box.prev
        bn = box.next
        bp.next = bn
        bn.prev = bp
        print(rid)
    elif cmd[0] == 400:
        fid = cmd[1]
        box = boxes.get(fid)
        if box is None:
            print(-1)
            continue
        bp = box.prev
        if bp.weight == 0:
            print(bp.id)
            continue
        belt_id = box.belt_id
        while belts[belt_id] is None:
            belt_id = belts_pointer[belt_id]
        head = belts[belt_id].head
        tail = belts[belt_id].tail
        hn = head.next
        tp = tail.prev

        head.next = box
        box.prev = head
        bp.next = tail
        tail.prev = bp
        tp.next = hn
        hn.prev = tp
        print(belt_id)
    elif cmd[0] == 500:
        bnum = cmd[1]
        broken_belt = belts[bnum]
        if broken_belt is None:
            print(-1)
            continue
        belts[bnum] = None
        new_belt_num = (bnum + 1) % len(belts)
        new_belt = belts[new_belt_num]
        while new_belt is None:
            new_belt_num = (new_belt_num + 1) % len(belts)
            new_belt = belts[new_belt_num]
        new_belt.pushall(broken_belt)
        belts_pointer[bnum] = new_belt_num
        print(bnum)

# 400 명령에서 뭉텅이를 앞으로 가지고 올 때 box.prev가 곧바로 head가 되는 경우에서 실수했다.
# 특히 링크드 리스트 문제에서 그림을 그려도 해당 element가 존재할 때 존재하지 않을 때를 잘 나눠서 생각하지 않으면 실수하는 것 같다.
# 저번에 했던 실수 또했는데 box -> 벨트 id 구하는 방법, 벨트 id 변경 테이블 관리해서 구하면 된다.
