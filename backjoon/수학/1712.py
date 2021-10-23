import sys

a, b, c = tuple(map(int, sys.stdin.readline().split()))

try:
    result = int(a / (c - b) + 1)
    if result < 0:
        print(-1)
    else:
        print(result)
except:
    print(-1)