# number_count = int(input())

# number_list = []
# for _ in range(number_count):
#     number = int(input())
#     number_list.append(number)

# number_list.sort()

# for i in number_list:
#     print(i)


import sys

a = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
a.sort()

for i in a:
    print(i)