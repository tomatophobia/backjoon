import sys
sys.stdin = open("input.txt", "r")

from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    D, W, K = map(int, input().rstrip().split())
    board = []
    for _ in range(D):
        board.append(list(map(int, input().rstrip().split())))
    candidate = [i for i in range(D)]
    ans = K
    for i in range(K):
        success = False
        if i == 0:
            all_success = True
            for w in range(W):
                seq = 1
                before = board[0][w]
                col_success = False
                for r in range(1, D):
                    if board[r][w] == before:
                        seq += 1
                    else:
                        seq = 1
                    before = board[r][w]
                    if seq == K:
                        col_success = True
                        break
                if not col_success:
                    all_success = False
                    break
            if all_success:
                success = True
                ans = i
                break
            else:
                continue
        for drug in combinations(candidate, i):
            for j in range(2 ** i):
                bb = bin(j)[2:]
                ab_drug = '0' * (i - len(bb)) + bb
                try_board = [board[copyd][:] for copyd in range(D)]
                for dd in range(len(drug)):
                    if ab_drug[dd] == '0':
                        try_board[drug[dd]] = [0] * W
                    else:
                        try_board[drug[dd]] = [1] * W
                all_success = True
                for w in range(W):
                    seq = 1
                    before = try_board[0][w]
                    col_success = False
                    for r in range(1, D):
                        if try_board[r][w] == before:
                            seq += 1
                        else:
                            seq = 1
                        before = try_board[r][w]
                        if seq == K:
                            col_success = True
                            break
                    if not col_success:
                        all_success = False
                        break
                if all_success:
                    success = True
                    break
            if success:
                ans = i
                break
        if success:
            break
    print(f'#{test_case} {ans}')

# python deepcopy 느리니까 대신 list comprehension 쓰자
