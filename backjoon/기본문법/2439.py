import sys

cnt = int(sys.stdin.readline().rstrip())

for n in range(1, cnt + 1):
    print(' ' * (cnt - n) + '*' * n)