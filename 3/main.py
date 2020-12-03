

def main():
    with open('input') as f:
        data = []
        for line in f.readlines():
            charArray = []
            data.append(charArray)
            for char in line:
                charArray.append(char)
        width = len(data[0])
        run = 3
        fall = 1
        row = 0
        column = 0
        treeCount = 0
        while row < len(data):
            if data[row][column%width] == "#":
                treeCount += 1
            row += fall
            column += run
        print(treeCount)



if __name__ == "__main__":
    main()