const assert = require("chai").assert;
const readTxt = require("../index");

describe("index.js", function () {
    it("should recieve Hello, World!", function () {
        const txt = readTxt();;
        assert.equal(txt, "Hello, World!");
    });
});
