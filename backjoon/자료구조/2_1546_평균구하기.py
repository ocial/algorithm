import sys

n = sys.stdin.readline().rstrip()
score_list = list(map(int, input().split()))
max_score = max(score_list)
total_score = sum(score_list)

print(total_score * 100 / max_score / int(n))