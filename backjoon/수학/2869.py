import sys
import math

a, b, v = tuple(map(int, sys.stdin.readline().split()))

print(math.ceil((v - a) / (a - b)) + 1)