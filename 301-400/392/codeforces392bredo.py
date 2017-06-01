bulbs = raw_input()


def fill_array(bb):
    Rc = 0
    Gc = 0
    Bc = 0
    Yc = 0
    R = -1
    G = -1
    B = -1
    Y = -1
    for i in range(0, len(bb)):
        if (bb[i] == "R"):
            R = i % 4
        elif (bb[i] == "G"):
            G = i % 4
        elif (bb[i] == "B"):
            B = i % 4
        elif (bb[i] == "Y"):
            Y = i % 4
    if (R == -1):
        R = 6 - B - G - Y
    elif (G == -1):
        G = 6 - B - R - Y
    elif (B == -1):
        B = 6 - R - G - Y
    elif (Y == -1):
        Y = 6 - B - G - R
    for i in range(0, len(bb)):
        if (bb[i] == "!"):
            x = i % 4
            if (x == R):
                Rc = Rc + 1
            elif (x == G):
                Gc = Gc + 1
            elif (x == B):
                Bc = Bc + 1
            elif (x == Y):
                Yc = Yc + 1
    print Rc, Bc, Yc, Gc

fill_array(bulbs)

