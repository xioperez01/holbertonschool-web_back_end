const assert = require("assert");
const calculateNumber = require("./0-calcul.js");

describe("calculateNumber", () => {
  it("Return sum of integers", () => {
    strictEqual(calculateNumber(1, 2), 3);
    strictEqual(calculateNumber(1, -1), 0);
    strictEqual(calculateNumber(1, -2), -1);
  });

  it("Round floats", () => {
    strictEqual(calculateNumber(1, 2.5), 4);
    strictEqual(calculateNumber(1.1, 2.5), 4);
    strictEqual(calculateNumber(1.5, 2.5), 5);
    strictEqual(calculateNumber(0.1, 0), 0);
    strictEqual(calculateNumber(1.4, -4.5), -3);
  });

  it("Return the rounded number if only one is provided", () => {
    strictEqual(calculateNumber(1), 1);
    strictEqual(calculateNumber(1.5), 2);
  });

  it("Cast non-numbers into numbers", () => {
    strictEqual(calculateNumber(true, "1"), 2);
    strictEqual(calculateNumber(1, "2.5"), 4);
    strictEqual(calculateNumber("1.2", 2.5), 4);
  });

  it("should throw typeerror if either param cannot be coerced to a number", () => {
    throws(() => calculateNumber("hello"), {
      name: "TypeError",
      message: "Parameters must be numbers",
    });
    throws(() => calculateNumber(1.2, "dog"), {
      name: "TypeError",
      message: "Parameters must be numbers",
    });
  });
});
