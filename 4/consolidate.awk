#!/usr/bin/awk -f

BEGIN {
FS = " "
}

{
    if ($0 == "") {
        print ""
    } else {
        printf $0
        printf " "
    }
}