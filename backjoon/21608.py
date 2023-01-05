import sys

input = sys.stdin.readline

N = int(input().rstrip())

students = []
for _ in range(N ** 2):
    x, a, b, c, d = map(int, input().rstrip().split(' '))
    students.append([x, [a, b, c, d]])

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
board = [[None] * N for _ in range(N)]
for student, loves in students:
    seat = [-1, -1]
    seat_score = [-1, -1]
    for r in range(N):
        for c in range(N):
            if board[r][c] is not None:
                continue
            score = [0, 0]
            for d in dirs:
                dr, dc = r + d[0], c + d[1]
                if dr < 0 or dr >= N or dc < 0 or dc >= N:
                    continue
                if board[dr][dc] is None:
                    score[1] += 1
                elif board[dr][dc] in loves:
                    score[0] += 1
            if seat_score < score:
                seat_score = score
                seat = [r, c]
    r, c = seat
    board[r][c] = student

satisfy = 0
for r in range(N):
    for c in range(N):
        loves = []
        for s, l in students:
            if s == board[r][c]:
                loves = l
        num = 0
        for d in dirs:
            dr, dc = r + d[0], c + d[1]
            if dr < 0 or dr >= N or dc < 0 or dc >= N:
                continue
            if board[dr][dc] in loves:
                num += 1
        if num >= 1:
            satisfy += 10 ** (num - 1)
print(satisfy)
