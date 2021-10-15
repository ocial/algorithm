import sys

num_list = [int(sys.stdin.readline().rstrip()) for _ in range(10)]

div_result = {num % 42 for num in num_list}

print(len(div_result))