# Please apply your effort before copying, pasting, and converting to your own version.

import math

a, b, c = input().split(',')

x1 = int(a+b+c)-int(a+b)
x2 = int('9'*len(c) + '0'*len(b))

n = x1 // math.gcd(x1, x2)
d = x2 // math.gcd(x1, x2)

print(n, '/', d)