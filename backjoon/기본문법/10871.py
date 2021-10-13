import sys

a, b = tuple(map(int, sys.stdin.readline().split()))
a_list = sys.stdin.readline().rstrip().split(' ')

for n in a_list:
    if int(n) < b:
        print(int(n), end=' ')
