cc = int(raw_input())
wel = map(int, raw_input().split(' '))

mm = max(wel)

ww = 0
for x in wel:
    y = mm - x
    ww = ww + y

print ww
