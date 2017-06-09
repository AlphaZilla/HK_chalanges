var string = "testCamelCase"
var count = 0

for (let x = 0; x < string.length; x++) {
    if (string[x] === string[x].toUpperCase()) {
        // console.log(string[x], "is upper case")
        count ++
    }
}

if (string[0]) {
    count ++
}

// console.log("nr", count)
console.log(count)

function testFunc(val) {
    return val
}

console.log(/[A-Z]/.test("teST"))
