import sys
from collections import deque

input = sys.stdin.readline


t = int(input())

qu = deque()

for i in range(t):
    cmd = input().rstrip().split(' ')
    if cmd[0] == 'push':
        qu.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(qu) > 0:
            sys.stdout.write(qu.popleft() + '\n')
        else:
            sys.stdout.write('-1\n')
    elif cmd[0] == 'size':
        sys.stdout.write(str(len(qu)) + '\n')
    elif cmd[0] == 'empty':
        if len(qu) == 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif cmd[0] == 'front':
        if len(qu) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(qu[0] + '\n')
    elif cmd[0] == 'back':
        if len(qu) == 0:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(qu[-1] + '\n')

'''
sys.stdout.write를 사용하면 print보다 더 빠르다고 한다. 대신 뒤에 \n을 붙여줘야 버퍼가 플러시 되는 듯
sys.stdout.write는 print로 aliasing이 잘 안되는 것 같은데 다른 방법 써보면 좋을 듯
python에서 list.pop(0)는 시간복잡도가 O(N)으로 느리다. 따라서 이 경우 deque를 사용하거나 따로 cursor를 관리해야 할 것 같다.
'''

