bulbs = raw_input()


def fill_array(bb):
    bx = []
    for i in range(0, len(bb)):
        done = False
        if (bb[i] == "!"):
            #print i
            m = i + 4
            while (m < len(bb)): #check four after
                if (bb[m] != "!"):
                    bx.append(bb[m])
                    #print bb[m]
                    done = True
                    break
                else:
                    m = m + 4
            if not done:
                n = i - 4
                #print "check"
                while (n > -1): #check four before
                    if (bb[n] != "!"):
                        bx.append(bb[n])
                        #print bb[n]
                        done = True
                        break
                    else:
                        n = n - 4
            if not done: #array only four
                lb = []
                if (i + 1 < len(bb)):
                    if (bb[i + 1] != "!"):
                        lb.append(bb[i + 1])
                if (i + 2 < len(bb)):
                    if (bb[i + 2] != "!"):
                        lb.append(bb[i + 2])
                if (i + 3 < len(bb)):
                    if (bb[i + 3] != "!"):
                        lb.append(bb[i + 3])
                if (i - 1 > 0):
                    if (bb[i - 1] != "!"):
                        lb.append(bb[i - 1])
                if (i - 2 < 0):
                    if (bb[i - 2] != "!"):
                        lb.append(bb[i - 2])
                if (i - 3 < 0):
                    if (bb[i - 3] != "!"):
                        lb.append(bb[i - 3])
                if lb.count('B') == 0:
                    bx.append('B')
                    #print 'B'
                elif lb.count('G') == 0:
                    bx.append('G')
                    #print 'G'
                elif lb.count('Y') == 0:
                    bx.append('Y')
                    #print 'Y'
                elif lb.count('R') == 0:
                    bx.append('R')
                    #print 'R'
    return bx

bq = fill_array(bulbs)

print bq.count('R'), bq.count('B'), bq.count('Y'), bq.count('G')
