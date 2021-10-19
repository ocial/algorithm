import sys
from collections import Counter

a = sys.stdin.readline().rstrip()

b  = Counter(a.lower()).most_common(2)

try: 
    if b[0][1] == b[1][1]:
        print('?')
    else:
        print(b[0][0].upper())
except:
    print(b[0][0].upper())