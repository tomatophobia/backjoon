import sys

input = sys.stdin.readline

t = int(input())

heap = []


def down(i, heap):
    cur = heap[i]
    left = heap[2 * i + 1] if 2 * i + 1 < len(heap) else 0
    right = heap[2 * i + 2] if 2 * i + 2 < len(heap) else 0

    if left >= right:
        if cur < left:
            heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
            down(2 * i + 1, heap)
    else:
        if cur < right:
            heap[i], heap[2 * i + 2] = heap[2 * i + 2], heap[i]
            down(2 * i + 2, heap)


def up(i, heap):
    if i != 0:
        cur = heap[i]
        prnt = heap[(i - 1) // 2]
        if prnt < cur:
            heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
            up((i - 1) // 2, heap)


for i in range(t):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heap[0])
        p = heap.pop()
        if len(heap) > 0:
            heap[0] = p
            down(0, heap)
    else:
        heap.append(x)
        up(len(heap) - 1, heap)
