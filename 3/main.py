

def main():
    with open('input') as f:
        lines = f.readlines()
        a = getTreeCount(lines, 1, 1)
        b = getTreeCount(lines, 3, 1)
        c = getTreeCount(lines, 5, 1)
        d = getTreeCount(lines, 7, 1)
        e = getTreeCount(lines, 1, 2)
        print(",".join(map(str, [a, b, c, d, e])))
        print(a*b*c*d*e)

def getTreeCount(lines, run, fall):
    rows = []
    for line in lines:
        columns = []
        rows.append(columns)
        for char in line:
            if char != "\n":
                columns.append(char)
    width = len(rows[0])
    row = 0
    column = 0
    treeCount = 0
    while row < len(rows):
        if rows[row][column%width] == "#":
            treeCount += 1
        row += fall
        column += run
    return treeCount

if __name__ == "__main__":
    main()