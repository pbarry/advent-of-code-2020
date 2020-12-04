import fileinput
import re

'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''

def isBetween(min, max):
    return lambda x: min <= int(x) <= max

def matchesRE(regex):
    return lambda s: re.search(regex, s) != None

def heightValidator(s):
    regex = re.compile("^([0-9]+)(cm|in)$")
    match = regex.search(s)
    if match == None:
        return False
    n = int(match.group(1))
    if match.group(2) == "cm":
        return 150 <= n <= 193
    else:
        return 59 <= n <= 76

def main():

    for line in fileinput.input():
        line = line.rstrip()
        if isLineValid(line):
            print("valid")
        else:
            print("invalid")

def isLineValid(line):
    print("")
    print(line)
    attrs = line.split(" ")
    requiredFields = {
        "byr": isBetween(1920, 2002),
        "iyr": isBetween(2010, 2020),
        "eyr": isBetween(2020, 2030),
        "hgt": heightValidator,
        "hcl": matchesRE("^#[0-9a-f]{6}$"),
        "ecl": matchesRE("^(amb|blu|brn|gry|grn|hzl|oth)$"),
        "pid": matchesRE("^[0-9]{9}$"),
    }
    for attr in attrs:
        split = attr.split(":")
        fieldName = split[0]
        if fieldName in requiredFields:
            if requiredFields[fieldName](split[1]):
                del requiredFields[fieldName]
            else:
                print("{0}:{1} failed".format(fieldName, split[1]))

    return len(requiredFields.keys()) == 0

if __name__ == "__main__":
    main()