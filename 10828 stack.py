import sys


def push(n):
    stack.append(n)


def pop():
    try:
        print(stack.pop())
    except:
        print(-1)


def size():
    return len(stack)


def empty():
    empty = 1 if len(stack) == 0 else 0
    print(empty)


def top():
    try:
        print(stack[-1])
    except:
        print(-1)


n = int(input())
stack = []
for i in range(n):
    cmd = sys.stdin.readline().split()
    print (cmd)
    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'pop':
        pop()
    elif cmd[0] == 'size':
        print(size())

    elif cmd[0] == 'empty':
        empty()

    elif cmd[0] == 'top':
        top()
