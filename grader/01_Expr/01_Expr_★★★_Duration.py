# Please apply your effort before copying, pasting, and converting to your own version.

a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

sum1 = a*60*60 + b*60 + c
sum2 = d*60*60 + e*60 + f

if sum2 < sum1:
  sum2 += 24*60*60
  
diff = sum2 - sum1 

print("{}:{}:{}".format(diff//(60*60), diff%(60*60)//60, diff%60))