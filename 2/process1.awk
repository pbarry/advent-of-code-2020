#!/usr/bin/awk -f

# Usage: ./process1.awk input | grep YAY | wc -l

function ltrim(s) { sub(/^[ \t\r\n]+/, "", s); return s }
function rtrim(s) { sub(/[ \t\r\n]+$/, "", s); return s }
function trim(s)  { return rtrim(ltrim(s)); }

BEGIN {
FS = ": "
print ""
}

{
    print $1, "|", $2
    spacePos = index($1, " ")
    countRange = substr($1,0,spacePos)
    letter = substr($1, spacePos+1)
    print countRange, letter
    split($2, chars, "")
    letterCount = 0
    for (i=1; i <= length($2); i++) {
        if (chars[i] == letter) {
            letterCount++
        }
    }
    print letterCount
    split(countRange, minmax, "-")
    min = int(minmax[1])
    max = int(minmax[2])
    print min, max
    if (letterCount >= min && letterCount <= max) {
        print "YAY"
    } else {
        print "boo"
    }
}

END {
print ""
}
