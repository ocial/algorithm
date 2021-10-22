# import re
# import sys

# total_cnt = int(sys.stdin.readline().rstrip())

# count = 0
# for _ in range(total_cnt):
#     a = sys.stdin.readline().rstrip()
#     b = a[0] + ''.join(a[i] for i in range(1, len(a)) if a[i-1] != a[i])

#     for x in set(b):
#         if len(re.findall(x, b)) != 1:
#             count += 1
#             break

# print(total_cnt - count)

result = 0
for _ in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1

print(result)