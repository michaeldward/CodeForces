xx = map(int, raw_input().split(' '))

m = xx[0]
mm = 0
d = xx[1]
c = 0

if m is 1 or m is 3 or m is 5 or m is 7 or m is 8 or m is 10 or m is 12:
    mm = 31
elif m is 2:
    mm = 28
else:
    mm = 30

mm = mm - 8 + d
c = c + 1

while (mm > 0):
    mm = mm - 7
    c = c + 1

print c
