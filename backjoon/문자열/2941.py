import re
import sys

a = sys.stdin.readline().rstrip()

cr_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
sc_term = '|'.join(cr_list)

print(len(re.sub(rf'({sc_term})', '@', a)))