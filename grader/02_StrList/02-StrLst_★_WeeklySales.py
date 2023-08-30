# Please apply your effort before copying, pasting, and converting to your own version.

x = input().split(' ')

x = sum(list(map(lambda x: int(x), filter(lambda x: x!='', x))))

print(x)