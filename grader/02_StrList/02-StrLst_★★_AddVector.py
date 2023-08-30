# Please apply your effort before copying, pasting, and converting to your own version.

i1, j1, k1 = input().replace('[', '').replace(']', '').replace(',', '').split(' ')
i2, j2, k2 = input().replace('[', '').replace(']', '').replace(',', '').split(' ')

v1 = [i1, j1, k1]
v2 = [i2, j2, k2]
v1 = list(map(lambda x: float(x), v1))
v2 = list(map(lambda x: float(x), v2))

v3 = [v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2]]

print(v1, '+', v2, '=', v3)