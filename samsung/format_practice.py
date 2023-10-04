board = [[100 * j + i for i in range(1, 101)] for j in range(100)]
# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in board]))

for x in range(100):
    for y in range(100):
        print(f'{board[x][y]:5}', end='')
    print('')
