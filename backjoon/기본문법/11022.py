import sys

cnt = int(sys.stdin.readline().rstrip())

for num in range(cnt):
    a, b = tuple(map(int, sys.stdin.readline().split()))
    print(f'Case #{num + 1}: {a} + {b} =', a + b)