import sys

a = int(sys.stdin.readline().rstrip())

for i in range(1, 10):
    print(f'{a} * {i} =', a*i)