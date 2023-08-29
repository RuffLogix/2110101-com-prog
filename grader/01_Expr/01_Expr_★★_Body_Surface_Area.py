# Please apply your effort before copying, pasting, and converting to your own version.

import math

w = float(input())
h = float(input())

ans1 = math.sqrt(w*h) / 60
ans2 = 0.024265 * w**(0.5378) * h**(0.3964)
ans3 = 0.0333 * w**(0.6157-0.0188*math.log10(w)) * h**(0.3)

print(ans1)
print(ans2)
print(ans3)