import sys

nn = sys.stdin.readline()
while(nn !=""):
    nn = nn.replace("\r", "").replace("\n", "")
    print("%s "%nn + "%s"%nn)
    nn = sys.stdin.readline()