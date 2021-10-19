import sys

a, b = tuple(map(str, sys.stdin.readline().split()))
c = int(''.join(reversed(a))), int(''.join(reversed(b)))
print(max(c))