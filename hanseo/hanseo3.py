import sys

tile_num = 1
current_tile = []
all_tiles = []
characters = []

D = int(input())
size = D

for line in sys.stdin:
    words = line.split(" ")
    x = []
    for word in words:
        word = word.strip()
        if word != '':
            x.append(word)
    characters += x

for char in characters:
    if char == '':
        characters.remove(char)
    if len(char) <= size:
        current_tile.append(char)
        size = len(char)
    else:
        all_tiles.append(current_tile)
        current_tile = []
        size = len(char)
        current_tile.append(char)

all_tiles.append(current_tile)  # 틀릴 수도 있음

for tile in all_tiles:
    width = len(tile[0])
    height = len(tile)
    parameters = [str(width), str(height), str(tile_num)]
    add = 0
    for par in parameters:
        if len(par) > add:
            add = len(par)
    header = ('+' + '-' * 9 + '-' * add + '-+')
    header_len = len(header)
    print(header)
    print('| Tile:' + ' ' * (header_len - 9 - len(str(tile_num))) + str(tile_num) + " |")
    tile_num += 1
    print('| Width:' + ' ' * (header_len - 10 - len(str(width))) + str(width) + " |")
    print('| Height:' + ' ' * (header_len - 11 - len(str(height))) + str(height) + " |")
    difference = (width + 2) - (header_len)
    if difference < 0:
        print('+' + '-' * width + '+' + '-' * (header_len - (width + 3)) + '+')
    elif difference == 0:
        print(header)
    elif difference == 1:
        print(header + '+')
    else:
        print(header + "-" * ((width + 1) - header_len) + '+')
    tile.reverse()
    for char in tile:
        if char != "":
            print("|" + " " * (width - len(char)) + char + '|')
        else:
            height -= 1
            continue
    print("+" + '-' * width + '+')
