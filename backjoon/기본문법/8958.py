import sys

a = int(sys.stdin.readline().rstrip())

for _ in range(a):
    zero_list = sys.stdin.readline().rstrip().split('X')
    zero_list = [len(zero) for zero in zero_list if len(zero) > 0]

    print(int(sum(num * (num + 1) / 2 for num in zero_list)))