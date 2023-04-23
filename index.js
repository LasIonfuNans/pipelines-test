const fs = require("fs");

const readTxt = () => {
    // このコード、突っ込までないでください。。。。
    const txt = fs.readFileSync(__dirname + "\\hello.txt", "utf8");
    return txt;
};

module.exports = readTxt;
