import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
exp = input()
numbers = []
operators = []
for i in range(N):
    if i % 2 == 0:
        numbers.append(exp[i])
    else:
        operators.append(exp[i])
max_p = -float('inf')
for i in range(2 ** (N // 2)):
    nums = numbers[:]
    ops = operators[:]
    bb = format(i, 'b')
    bb = '0' * (N // 2 - len(bb)) + bb
    if '11' in bb:
        continue
    for b in range(len(bb) - 1, -1, -1):
        if bb[b] == '1':
            r = eval(nums[b] + ops[b] + nums[b+1])
            nums[b] = str(r)
            nums.pop(b + 1)
            ops.pop(b)
    result = nums[0]
    for j in range(1, len(nums)):
        result = str(eval(result + ops[j-1] + nums[j]))
    result = int(result)
    if max_p < result:
        max_p = result
print(max_p)
