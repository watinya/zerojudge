import sys

a = []
for n in sys.stdin:
    p = input()
    p = p.split()
    for s in range(int(len(p))):
        mm = (min(list(map(int , p))))
        print(mm , end = " ")
        p.remove("%s"%mm)
    print()