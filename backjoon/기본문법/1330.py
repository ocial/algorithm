import sys
A, B = tuple(map(int, sys.stdin.readline().split()))

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')