import sys

array = []
rowcol = sys.stdin.readline()
while(rowcol != ""):
    rowcol = rowcol.split()
    
    for row in range(int(rowcol[0])):
        row = sys.stdin.readline()
        row = row.strip("\n")
        row = row.split()
        array.append(row)
    
    change = sys.stdin.readline()
    change = change.split()[::-1]
    for s in range(int(rowcol[2])):
        if (int(change[s]) == 0):
            array = list(map(list,zip(*array)))
            array.reverse()
        else:
            array.reverse()
    
    print(len(array) , len(array[0]))
    
    for row in range(len(array)):
        p = []
        for col in range(len(array[row])):
            p.append(array[row][col])
        print(" ".join(p),end = "")
        print()
    
    rowcol = sys.stdin.readline()
    array = []