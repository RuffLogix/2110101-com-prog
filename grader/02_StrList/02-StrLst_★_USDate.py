# Please apply your effort before copying, pasting, and converting to your own version.

d, m, y = input().split('/')

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print(month[int(m)-1], d+',', y)