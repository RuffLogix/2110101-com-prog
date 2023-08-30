# Please apply your effort before copying, pasting, and converting to your own version.

x = input()
n = int(input())

print(max(0, n-len(x))*'0' + x)