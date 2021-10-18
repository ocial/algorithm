import sys

while True:
    a = sys.stdin.readline().split()
    if len(a) > 1:
        a, b = a[0], a[1]
        print(''.join([n * int(a) for n in list(b)]))            
    elif len(a) == 1:
        pass
    else:
        break