const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on("line", (line) => {
    words = line.trim().split(" ");
    console.log(words[0] === ''? 0 : words.length);

    rl.close();
}).on("close", () => {
    process.exit();
})

