const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on("line", (line) => {
    result = []
    for(let i=97; i<123; i++) {
        alp = String.fromCharCode(i);
        result.push(line.indexOf(alp));
    }
    console.log(result.join(' '))

}).on("close", () => {
    process.exit();
})
