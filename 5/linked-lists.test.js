const { expect } = require("@jest/globals");
const { LinkedListOfInts } = require("./linked-lists.js");

test("LinkedListOfInts", () => {
    const list = new LinkedListOfInts();
    list.add(1);
    list.add(2);
    list.add(3);
    expect(list.toArray()).toStrictEqual([1,2,3]);
});
