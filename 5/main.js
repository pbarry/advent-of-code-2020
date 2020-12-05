const { LinkedListOfInts } = require("./linked-lists.js");
const { getSeatId } = require("./seat-utils.js");

const fs = require('fs')

fs.readFile('input', 'utf8' , (err, data) => {
    if (err) {
        console.error(err)
        return
      }
      const lines = data.split(/\r\n|\r|\n/);
      let maxSeatId = 0;
      for (i in lines) {
        const l = lines[i]
        const seatId = getSeatId(l);
        if (seatId > maxSeatId) {
            maxSeatId = seatId;
        }
      }
      console.log("Max Seat ID: " + maxSeatId);

      // Part 2
      let allSeatIds = new LinkedListOfInts();
      for (i in lines) {
        const l = lines[i];
        const seatId = getSeatId(l);
        allSeatIds.add(seatId);
      }
      // allSeatIds.print();
      let current = allSeatIds.firstNode;
      while (current.next) {
        if (current.next.n > current.n + 1) {
            console.log(`Found gap between ${current.n} and ${current.next.n}`);
        }
        current = current.next
      }
});
