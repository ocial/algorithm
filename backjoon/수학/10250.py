import sys
from math import ceil

for _ in range(int(input())):
    h, w, n = tuple(map(int, sys.stdin.readline().split()))

    f = n % h
    print(str(f if f != 0 else h) + str(ceil(n / h)).zfill(2))