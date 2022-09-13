import sys
tile_num = 1
current_tile = []

for line in sys.stdin:
    words = line.split(" ")
    for word in words:
        word = word.strip()
        if len(word) == 0:
            continue
        if len(current_tile) == 0 or len(current_tile[-1]) >= len(word):
            current_tile.append(word)
        else:
            header_length = max(6 + len(str(tile_num)), 7 + len(str(len(current_tile[0]))),
                                8 + len(str(len(current_tile))))
            header_length += 4
            print("+" + "-" * (header_length - 2) + "+")
            print("| Tile:" + str(tile_num).rjust(header_length - 9) + " |")
            print("| Width:" + str(len(current_tile[0])).rjust(header_length - 10) + " |")
            print("| Height:" + str(len(current_tile)).rjust(header_length - 11) + " |")

            body_length = len(current_tile[0]) + 2
            s = min(header_length,body_length)
            l = max(header_length, body_length)
            mid = "+" + "-"*(s-2) + "+"
            if l-s-1 > 0:
                mid += "-"*(l-s-1)
            if l-s > 0:
                mid += "+"
            print(mid)
            for w in range(len(current_tile) - 1, -1, -1):
                print("|" + current_tile[w].rjust(body_length-2) + "|")
            print("+" + "-"*(body_length-2) + "+")
            tile_num += 1
            current_tile = [word]


