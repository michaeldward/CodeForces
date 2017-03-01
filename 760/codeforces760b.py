xx = map(int, raw_input().split(' '))


n = xx[0]
m = xx[1]
k = xx[2]

p = 0
if (m >= n):
    m = m - n
    p = 1
if (m > 0):
    m = m - 1
    p = 2

a = n - k
if (a < k): #Frodo on right of middle (a == 0 if very right)
    x = 1
    q = 1
    #print "right"
    while (m > 0):
        if (x >= n):
            x = n
        elif (k + q >= n + 1): #right side reached
            #print "right side reached"
            x = x + 1
        else:
            x = x + 2
            q = q + 1
        if (m >= x):
            #print "adding ", p, " pillows"
            p = p + 1
            m = m - x
        else:
            m = 0

else: #Frodo on left of middle (a == n-1 if very left)
    x = 1
    q = 1
    #print "left"
    while (m > 0):
        if (x >= n):
            #print "x is n"
            x = n
        elif (k - q <= 0): #left side reached
            #print "left side reached"
            x = x + 1
        else:
            x = x + 2
            q = q + 1
        if (m >= x):
            #print "adding ", p, " pillows"
            p = p + 1
            m = m - x
        else:
            m = 0
    

print p
