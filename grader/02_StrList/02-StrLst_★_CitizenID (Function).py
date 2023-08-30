# Please apply your effort before copying, pasting, and converting to your own version.

def check_digit(x):
    return (11 - sum([(13-int(i)) * int(v) for (i, v) in enumerate(x)]) % 11) % 10

exec(input())