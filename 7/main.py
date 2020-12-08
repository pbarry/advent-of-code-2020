import fileinput
import re

# Usage: cat input | python3 main.py

contentsOf = {}
containersOf = {}

def main():
    for line in fileinput.input():
        split = line.split(" bags contain ")
        containingColor = split[0]
        containsList = split[1].split("bag")
        containsList = [x.strip(" ,.s") for x in containsList]
        print("{0} contains: ".format(containingColor))
        for contain in containsList:
            if len(contain.strip()) == 0:
                continue
            regex = re.compile("([0-9]+) ([a-z ]+)")
            result = regex.search(contain)
            containedColor = None
            if result is not None:
                containedColor = result.group(2)
                if containedColor not in containersOf:
                    containersOf[containedColor] = []
                containersOf[containedColor].append(containingColor)
                for _ in range(0, int(result.group(1))):
                    if containingColor not in contentsOf:
                        contentsOf[containingColor] = []
                    contentsOf[containingColor].append(containedColor)
            print("   {0}".format(containedColor))
    # Part 1
    validContainers = []
    queue = containersOf["shiny gold"].copy()
    while len(queue) > 0:
        validContainers.append(queue[0])
        if queue[0] in containersOf:
            for c in containersOf[queue[0]]:
                if c not in validContainers and c not in queue:
                    queue.append(c)
        del queue[0]
    print(validContainers)
    print(len(validContainers))
    # Part 2
    containees = []
    queue = contentsOf["shiny gold"].copy()
    while len(queue) > 0:
        c = queue[0]
        containees.append(c)
        if c in contentsOf:
            for next in contentsOf[c]:
                queue.append(next)
        del queue[0]
    print("Part 2")
    print(containees)
    print(len(containees))
        

if __name__ == "__main__":
    main()