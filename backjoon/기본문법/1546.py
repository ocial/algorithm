import sys

total_cnt = int(sys.stdin.readline().rstrip())
score_list = list(map(int, sys.stdin.readline().rstrip().split()))

fake_average = sum(score/max(score_list)*100 for score in score_list) / total_cnt
print(fake_average)