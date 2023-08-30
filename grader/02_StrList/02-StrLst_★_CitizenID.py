# Please apply your effort before copying, pasting, and converting to your own version.

x = input()

print(x[0], x[1:5], x[5:10], x[10:], (11 - sum([(13-int(i)) * int(v) for (i, v) in enumerate(x)]) % 11) % 10)