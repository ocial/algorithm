import sys
input = sys.stdin.readline

a, b = map(int, input().split())

c = list(map(int, input().split()))

d = 0
e = [0]
for i in c:
    d += i
    e.append(d)

for _ in range(b):
    x, y = map(int, input().split())
    print(e[y] - e[x-1])