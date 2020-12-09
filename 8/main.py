import fileinput

def main():
    instructions = []
    lines = []
    for line in fileinput.input():
        lines.append(line)
        parts = line.split(" ")
        instructions.append({
            "cmd": parts[0],
            "num": int(parts[1])
        })
    history = []
    current = 0
    sum = 0
    while current not in history:
        i = instructions[current]
        history.append(current)
        cmd = i["cmd"]
        if cmd == "acc":
            sum += i["num"]
            current += 1
        if cmd == "nop":
            current += 1
        if cmd == "jmp":
            current += i["num"]
    print("Sum before looping = {}".format(sum))
    # part 2
    swap_candidates = [index for index, i in enumerate(instructions) if i["cmd"] in ["nop", "jmp"]]
    print("Swap candidates: {}".format(swap_candidates))
    swap_candidate_iter = iter(swap_candidates)
    success = False
    while not success:
        swap_candidate = next(swap_candidate_iter)
        history = []
        current = 0
        sum = 0
        while current not in history:
            print("   Instruction {}".format(current))
            if current >= len(instructions):
                print("Successful exit! Accumulator is {}".format(sum))
                success = True
                break
            i = instructions[current]
            history.append(current)
            cmd = i["cmd"]
            if cmd == "acc":
                sum += i["num"]
                current += 1
                continue
            if swap_candidate == current:
                print("Trying to swap line {0}, instruction {1}".format(swap_candidate, i))
                if cmd == "jmp":
                    cmd = "nop"
                else:
                    cmd = "jmp"
            if cmd == "nop":
                current += 1
            if cmd == "jmp":
                current += i["num"]
    

if __name__ == "__main__":
    main()