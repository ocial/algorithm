import sys

a = int(sys.stdin.readline().rstrip())

answer = 0
for i in range(1, a + 1):
    answer += i

print(answer)
