import sys


def get_horizontal_line(block):
    headline = "+"
    for tile in block:
        word = tile[0]
        headline += "-" * len(word)
        headline += "+"
    return headline


def merge_horizontal_line(hline1, hline2):
    # +--+-----+---+
    # +-----+----+----+
    merged = ""
    longer = hline1 if len(hline1) > len(hline2) else hline2
    shorter = hline1 if len(hline1) <= len(hline2) else hline2

    for i in range(len(shorter)):
        c1 = shorter[i]
        c2 = longer[i]
        if c1 == '-' and c2 == '-':
            merged += '-'
        else:
            merged += '+'

    for i in range(len(shorter), len(longer)):
        merged += longer[i]
    return merged

def get_inner_block(block, current_height):
    inner = ""
    for i in range(current_height):
        temp = "\n|"
        for ttile in block:
            twidth = len(ttile[0])
            if i < len(ttile):
                temp += " " * (twidth - len(ttile[i])) + ttile[i] + "|"
            else:
                temp += " " * twidth + "|"
        inner = temp + inner
    inner = inner.strip()
    return inner

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


before_hline = ""
block = []
current_block_len = 1
current_height = 0
for tile in all_tiles:
    width = len(tile[0])
    height = len(tile)

    next_block_len = current_block_len + width + 1

    if next_block_len <= D:
        block.append(tile)
        current_block_len = next_block_len
        if height > current_height:
            current_height = height
    else:
        # block에 있는 것을 프린트
        hline = get_horizontal_line(block)
        mhline = merge_horizontal_line(before_hline, hline)
        print(mhline)

        inner = get_inner_block(block, current_height)
        print(inner)

        # 초기화
        before_hline = hline
        block = []
        current_block_len = 1
        current_height = 0
        # 타일 하나를 블록에 넣음
        block.append(tile)
        current_block_len = current_block_len + width + 1
        if height > current_height:
            current_height = height

# 남은 block은 전부 프린트
hline = get_horizontal_line(block)
mhline = merge_horizontal_line(before_hline, hline)
print(mhline)

inner = get_inner_block(block, current_height)
print(inner)

print(hline)
