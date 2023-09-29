import sys
sys.stdin = open("input.txt", "r")

T = int(input())
four = [[0, 1], [0, -1], [-1, 0], [1, 0]]
for test_case in range(1, T + 1):
    N = int(input())
    particles = []
    for _ in range(N):
        x, y, d, k = map(int, input().rstrip().split())
        particles.append([x, y, d, k])
    total_energy = 0
    while len(particles) > 0:
        next_particles = []
        crashes = {}
        to_die = set()
        for x, y, d, k in particles:
            nx, ny = x + four[d][0] * 0.5, y + four[d][1] * 0.5
            if -1000 <= nx <= 1000 and -1000 <= ny <= 1000:
                l = crashes.get((nx, ny))
                if l is not None:
                    to_die.add((nx, ny))
                if l is None:
                    l = []
                    crashes[(nx, ny)] = l
                next_particles.append([nx, ny, d, k])
                l.append(k)
        for diex, diey in to_die:
            total_energy += sum(crashes.get((diex, diey)))
            next_particles = filter(lambda p: [p[0], p[1]] != [diex, diey], next_particles)
        particles = list(next_particles)
    print(f'#{test_case} {total_energy}')
