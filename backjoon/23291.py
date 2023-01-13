import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().rstrip().split(' '))

fishes = list(map(lambda s: [int(s)], input().rstrip().split(' ')))
count = 0
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
while True:
    max_f = -float("inf")
    min_f = float("inf")
    for [f] in fishes:
        if f > max_f:
            max_f = f
        if f < min_f:
            min_f = f
    if max_f - min_f <= K:
        break
    # add fish
    for i in range(len(fishes)):
        if fishes[i][0] == min_f:
            fishes[i][0] += 1
    # roll
    fishes[1].append(fishes[0][0])
    fishes[0] = []
    start = 1
    end = 2
    while len(fishes[start]) <= len(fishes) - end:
        temp = len(fishes[start])
        for i in range(end - 1, start - 1, -1):
            for j in range(len(fishes[i])):
                fishes[end + j].append(fishes[i][j])
            fishes[i] = []
        start, end = end, end + temp
    # move fish
    new_fishes = [[0] * N for _ in range(N)]
    for i in range(len(fishes)):
        for j in range(len(fishes[i])):
            left = fishes[i][j]
            for d in dirs:
                di, dj = i + d[0], j + d[1]
                if di < 0 or di >= N or dj < 0 or dj >= len(fishes[di]):
                    continue
                m = (fishes[i][j] - fishes[di][dj]) // 5
                if m > 0:
                    new_fishes[di][dj] += m
                    left -= m
            new_fishes[i][j] += left
    fishes = [[] for _ in range(N)]
    k = 0
    for i in range(len(new_fishes)):
        for j in range(len(new_fishes[i])):
            if new_fishes[i][j] != 0:
                fishes[k].append(new_fishes[i][j])
                k += 1
    # half and half
    for i in range(N // 2):
        fishes[N // 2 + i].append(fishes[N // 2 - i - 1][0])
        fishes[N // 2 - i - 1] = []
    for i in range(N // 4):
        fishes[(N * 3) // 4 + i].append(fishes[(N * 3) // 4 - i - 1][1])
        fishes[(N * 3) // 4 + i].append(fishes[(N * 3) // 4 - i - 1][0])
        fishes[(N * 3) // 4 - i - 1] = []
    # move fish
    new_fishes = [[0] * N for _ in range(N)]
    for i in range(len(fishes)):
        for j in range(len(fishes[i])):
            left = fishes[i][j]
            for d in dirs:
                di, dj = i + d[0], j + d[1]
                if di < 0 or di >= N or dj < 0 or dj >= len(fishes[di]):
                    continue
                m = (fishes[i][j] - fishes[di][dj]) // 5
                if m > 0:
                    new_fishes[di][dj] += m
                    left -= m
            new_fishes[i][j] += left
    fishes = [[] for _ in range(N)]
    k = 0
    for i in range(len(new_fishes)):
        for j in range(len(new_fishes[i])):
            if new_fishes[i][j] != 0:
                fishes[k].append(new_fishes[i][j])
                k += 1
    count += 1
print(count)
