import sys

s = sys.stdin.readline()
s = s.replace("\n","")
t = 1
while(s != "#"):
    s = s.replace("\n","")
    if (s == "HELLO"):
        print("Case %d: ENGLISH"%t)
    elif(s == "HOLA"):
        print("Case %d: SPANISH"%t)
    elif(s == "HALLO"):
        print("Case %d: GERMAN"%t)
    elif(s == "BONJOUR"):
        print("Case %d: FRENCH"%t)
    elif(s == "CIAO"):
        print("Case %d: ITALIAN"%t)
    elif(s == "ZDRAVSTVUJTE"):
        print("Case %d: RUSSIAN"%t)
    else:
        print("Case %d: UNKNOWN"%t)
    t += 1
    s = sys.stdin.readline()