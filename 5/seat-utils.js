const findRow = function(s) {
    return binarySearch(s, "B");
}
const findCol = function(s) {
    return binarySearch(s, "R");
}
const binarySearch = function(s, highChar) {
    r = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] == highChar) {
            r +=  Math.pow(2, s.length - i - 1);
        }
    }
    return r;
}
const getSeatId = function(s) {
    return findRow(s.slice(0,7)) * 8 + findCol(s.slice(7,10));
}

exports.findRow = findRow;
exports.findCol = findCol;
exports.getSeatId = getSeatId;