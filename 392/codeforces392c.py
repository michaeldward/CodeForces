aa = map(int, raw_input().split(' '))

mn = 0
mx = 0
sg = 0

top = 0
mid = 0
btm = 0


def check_sergio():
    return -1

n = aa[0]
m = aa[1]
k = aa[2]
x = aa[3]
y = aa[4]

q = k
a = n * m
b = (n - 1) * m

if (b == 0):
    mn = k % m
    mx = mn + 1
    sg = check_sergio()
elif (q > a):
    down = True
    q = q - a
    top = top + 1
    mid = mid + 1
    btm = btm + 1
    mdd = q / b
    lt = q % b
    mid = mid + mdd
    top = top + (mdd / 2)
    btm = btm + (mdd - (mdd / 2))
    end = q % b
    if (mdd % 2 == 0):
        down = False
    if (lt > m): #in mid
        mx = mid + 1
        if down: #in top
            mn = btm
        else: #in bottom
            mn = top
    elif (lt > 0):
        mx = mid
        if down: #in top
            mn = btm
        else: #in bottom
            mn = top
    sg = check_sergio()
else:
    mn = 0
    mx = 1
    sg = check_sergio()
print mx, mn, sg
