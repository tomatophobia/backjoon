import sys
sys.stdin = open("input.txt", "r")

dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
T = int(input().rstrip())
for test_case in range(1, T + 1):
    N = int(input().rstrip())
    atoms = []
    for _ in range(N):
        atoms.append(list(map(int, input().rstrip().split(' '))))

    energy = 0
    while len(atoms) > 0:
        next_atoms = {}
        for x, y, d, e in atoms:
            dx, dy = x + dirs[d][0] * 0.5, y + dirs[d][1] * 0.5
            if dx < -1000 or dx > 1000 or dy < -1000 or dy > 1000:
                continue
            key = (dx * 2 + 2000) * 10000 + (dy * 2 + 2000)
            if key in next_atoms:
                next_atoms[key].append([dx, dy, d, e])
            else:
                next_atoms[key] = [[dx, dy, d, e]]
        next_next = []
        for k in next_atoms:
            if len(next_atoms[k]) > 1:
                for _, _, _, e in next_atoms[k]:
                    energy += e
            else:
                next_next.append(next_atoms[k][0])
        atoms = next_next
    print(f"#{test_case} {energy}")
