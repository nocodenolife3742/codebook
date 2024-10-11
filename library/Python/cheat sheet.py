# input
n = int(input())
l = [int(x) for x in input().split()]

# EOF
while True:
    try:
        input()
    except:
        break

# output
print([1, 2, 3], [4, 5, 6], sep=' ', end='')
print(' '.join(str(x) for x in [1, 2, 3]))
print(f'{0.111111: .3f}')

# ascii
ord('c')
chr(97)

# list
l = [x for x in range(3)]
l.append(4)

# sort
l.sort(reverse=True)
sorted(l, key=lambda x: x)

# dict
d = {1: "a"}
d['2'] = '3'
for k, v in d.items():
    print(k, v)
1 in d

# deque
from collections import deque
q = deque([3, 4, 5])
q.appendleft(2)
q.append(6)
q.popleft()
q.pop()
q[0]

# random
from random import *
randint(1, 10)
choice([1, 2, 3])
shuffle([1, 2, 3])

# Decimal
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 250
d = Decimal('0.3') # check -0 when output
f = Fraction(d)
f.numerator
f.denominator

# fast input
import io, os, sys
input = sys.stdin.readline
# call input().decode() to convert into string
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 

# fast output
import sys
sys.stdout.write("need to be string")
