const { expect } = require("@jest/globals");
const { findRow, findCol, getSeatId } = require("./seat-utils.js");

test("find row tests", () => {
  expect(findRow("FFFFFFF")).toBe(0);
  expect(findRow("FBFFFFF")).toBe(32);
  expect(findRow("FFBFFFF")).toBe(16);
  expect(findRow("FFFBFFF")).toBe(8);
  expect(findRow("FFFFBFF")).toBe(4);
  expect(findRow("FFFFFBF")).toBe(2);
  expect(findRow("FFFFFFB")).toBe(1);
  expect(findRow("BFFFFFF")).toBe(64);
  expect(findRow("BBFFFFF")).toBe(64+32);
  expect(findRow("BFBFFFF")).toBe(64+16);
  expect(findRow("BFFBFFF")).toBe(64+8);
  expect(findRow("BFFFBFF")).toBe(64+4);
  expect(findRow("BFFFFBF")).toBe(64+2);
  expect(findRow("BFFFFFB")).toBe(64+1);
});
test("find col tests", () => {
  expect(findCol("LLL")).toBe(0);
  expect(findCol("RLL")).toBe(4);
  expect(findCol("LRL")).toBe(2);
  expect(findCol("LLR")).toBe(1);
});
test("getSeatId", () => {
    expect(getSeatId("FFFFFFFLLL")).toBe(0);
    expect(getSeatId("FFFFFFFRLL")).toBe(4);
    expect(getSeatId("BFFFFFFLLL")).toBe(64*8);
});