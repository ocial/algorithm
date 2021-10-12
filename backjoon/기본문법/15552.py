import sys

cnt = int(sys.stdin.readline().rstrip())

for _ in range(cnt):
    a, b = tuple(map(int, sys.stdin.readline().split()))
    print(a + b)