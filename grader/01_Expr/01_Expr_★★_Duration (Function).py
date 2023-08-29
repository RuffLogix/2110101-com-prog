# Please apply your effort before copying, pasting, and converting to your own version.

def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])

def hms2str(h, m, s):
    return ('0'+str(h))[-2:] + ':' + \
        ('0'+str(m))[-2:] + ':' + \
        ('0'+str(s))[-2:]

def to_sec(h, m, s):
    return h*(60*60) + m*60 + s
 
def to_hms(s):
    h = s//(60*60)
    m = (s%(60*60))//60
    s = s%(60*60)%60

    return h, m, s

def diff(h1, m1, s1, h2, m2, s2):
    t1, t2 = to_sec(h1, m1, s1), to_sec(h2, m2, s2)
    dt = abs(t1 - t2)

    return to_hms(dt)

def main():
    hms_start = input()
    hms_end = input()

    h1, m1, s1 = str2hms(hms_start)
    h2, m2, s2 = str2hms(hms_end)

    dt = diff(h1, m1, s1, h2, m2, s2)

    print(hms2str(dt[0], dt[1], dt[2]))

exec(input()) 