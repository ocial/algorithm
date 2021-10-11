import sys
h, m = tuple(map(int, sys.stdin.readline().split()))

time = h * 60 + m - 45
if time < 0:
    time += 24 * 60
    
print(time // 60, time % 60)