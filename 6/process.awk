#!/usr/local/bin/gawk -f

# Usage: ./process.awk input

BEGIN {
    FS = ""
    GROUP_ID = 0
}

{
    if ($0 == "") {
        GROUP_ID ++
        next
    }
    if (!GROUP_LENGTHS[GROUP_ID]) {
        GROUP_LENGTHS[GROUP_ID] = 0
    }
    GROUP_LENGTHS[GROUP_ID] ++
    split($0, chars, "")
    for (i in chars) {
        c = chars[i]
        if (!GROUPS[GROUP_ID][c]) {
            GROUPS[GROUP_ID][c] = 0
        }
        GROUPS[GROUP_ID][c] ++
        print "Group", GROUP_ID, "Char", c, "Count", GROUPS[GROUP_ID][c]
    }
}

END {
    total = 0
    total_everyone = 0
    for (i in GROUPS) {
        total += length(GROUPS[i])
        for (c in GROUPS[i]) {
            if (GROUPS[i][c] == GROUP_LENGTHS[i]) {
                print "Group", i, ", Char", c, "Count", GROUPS[i][c], "Matches people count", GROUP_LENGTHS[i]
                total_everyone ++
            } else {
                print "Group", i, ", Char", c, "Count", GROUPS[i][c], "DOESN'T match people count", GROUP_LENGTHS[i]
            }
        }
    }
    print ""
    print "Sum of group lengths is", total
    print "Sum of group lengths where everyone answers yes is", total_everyone
}
