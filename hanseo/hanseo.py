import math

l_node = 0
e_node = 0
r_node = 0


class Node:
    def __init__(self, color):
        self.parent = None
        self.left = None
        self.right = None
        self.color = color

        self.complete = False
        self.left_black = None
        self.left_white = None
        self.right_black = None
        self.right_white = None


def count_bnw(node):
    global l_node
    global e_node
    global r_node
    if node.complete:
        return [node.left_black, node.left_white, node.right_black, node.right_white]
    lc = [0, 0, 0, 0]  # left node 제외 하위 트리의 black, white 상태
    rc = [0, 0, 0, 0]
    lbw = -1  # left node가 black이냐 화이트냐
    rbw = -1
    if node.left is not None:
        lc = count_bnw(node.left)
        lbw = node.left.color
    if node.right is not None:
        rc = count_bnw(node.right)
        rbw = node.right.color
    result = [lc[0] + lc[2], lc[1] + lc[3], rc[0] + rc[2], rc[1] + rc[3]]

    if lbw == 0:
        result[1] += 1
    elif lbw == 1:
        result[0] += 1

    if rbw == 0:
        result[3] += 1
    elif rbw == 1:
        result[2] += 1

    node.left_black = result[0]
    node.left_white = result[1]
    node.right_black = result[2]
    node.right_white = result[3]
    node.complete = True

    if result[0] > 0 and result[1] > 0 and result[2] > 0 and result[3] > 0:
        a = result[1] / result[0]
        b = result[3] / result[2]
        if a > b:
            l_node += 1
        elif a == b:
            e_node += 1
        else:
            r_node += 1
    return result


if __name__ == '__main__':
    N = int(input().strip())
    colors = list(map(int, input().split()))
    node_list = list(map(lambda x: Node(x), colors))

    for i in range(N - 1):
        edge = list(map(int, input().split()))
        if edge[2] == 0:  # left
            node_list[edge[0]].left = node_list[edge[1]]
            node_list[edge[1]].parent = node_list[edge[0]]
        elif edge[2] == 1:  # right
            node_list[edge[0]].right = node_list[edge[1]]
            node_list[edge[1]].parent = node_list[edge[0]]

    count_bnw(node_list[0])
    print(l_node, e_node, r_node)
