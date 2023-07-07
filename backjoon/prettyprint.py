def prettyprint(board):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
