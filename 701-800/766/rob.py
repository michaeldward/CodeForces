while True:
    a = raw_input()
    b = raw_input()
    if len(a) and len(b) > 100000:
        print 'Error'
    else:
        break
    
def lcs(a, b, m, n):
 
    if m == 0 or n == 0:
       return 0;
    elif a == b:
       return -1
    elif a != b:
        if len(a) > len(b):
            return len(a)
        return len(b)

print lcs(a, b, len(a), len(b))
