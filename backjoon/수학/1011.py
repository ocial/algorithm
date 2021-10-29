import sys
from math import ceil, floor

for _ in range(int(input())):
    x, y = tuple(map(int, sys.stdin.readline().split()))

    if y - x == 2:
        print(2)
        continue

    n = ceil((y - x) ** 0.5) - 1

    if y - x <= n * (n + 1):
        print(2 * n)
    else:
        print(2 * n + 1)