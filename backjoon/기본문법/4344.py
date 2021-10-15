import sys

a = int(sys.stdin.readline().rstrip())

for _ in range(a):
    exam_list = list(map(int, sys.stdin.readline().rstrip().split()))
    exam_mean = sum(exam_list[1:]) / exam_list[0]

    percent = len([score for score in exam_list[1:] if score > exam_mean]) / exam_list[0] * 100
    print('{:.3f}%'.format(percent))