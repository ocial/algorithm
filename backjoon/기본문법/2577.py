import sys
from collections import Counter

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())

multiply = a * b * c

count_num = Counter(str(multiply))

for num in range(10):
    print(count_num[str(num)])