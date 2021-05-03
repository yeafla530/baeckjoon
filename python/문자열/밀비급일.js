// const fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let a = 'hello'
let lst = new Array()
for (let i = 0; i < input.length; i++){
    a = input[i]
    lst.push(a.split('').reverse().join(''))
}
for (let i = 0; i < lst.length; i++) {
    console.log(lst[i])
}