# Please apply your effort before copying, pasting, and converting to your own version.

x = input()

x1 = int(x[3::7])
x2 = int(x[7::5])

result = str(x1+x2+10000)[-4:-1]
sum = 0

for i in result:
    sum += int(i)

print(result+chr(sum%10+1+ord('A')-1))