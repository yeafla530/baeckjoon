 // 백준
// 앞서 얘기한대로 백준에서도 구름처럼 readline으로 읽어들이는게 가능하지만 느리다고 한다.
// 공식적으로 권장 되는 방법인 fs를 쓰자.

// 입력 코드
// const fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

// console.log(input);
// test case
// good morning
// hello world!
// 테스트 케이스는 파일로 존재하고, fs.readFileSync('/dev/stdin').toString() 를 통해 good morning\nhello world!\n 라는 문자열을 읽어들인다.
// 여기서 split을 통해 문자열을 \n 기준으로 끊어 배열로 반환한다.

// 그렇게 되면 input = ['good morning', 'hello world!']과 같이 input 배열에 한 줄씩
// 

// const fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');


const a = '11:59:48'
const b = '21:30:21'

let t1 = []
let t2 = []
let time1 = 0
let time2 = 0
let realTime = 0

t1 = a.split(':')
t2 = b.split(':')

time1 = t1[0]*60*60 + t1[1]*60 + t1[2]*1
time2 = t2[0]*60*60 + t2[1]*60 + t2[2]*1

if (time2 >= time1) {
    realTime = time2 - time1
} else {
    realTime = time2 - time1 + 24*60*60
}

let h = 0, m=0, s=0
let result = ''
h = parseInt(parseInt(realTime / 60) / 60)
m = parseInt(realTime / 60) % 60
s = realTime % 60

// console.log(h, m, s)
h = h.toString()
m = m.toString()
s = s.toString()
// console.log(h)
if (h.length == 1) {h = '0' + h}
if (m.length == 1) {m = '0' + m}
if (s.length == 1) {s = '0' + s}

console.log(`${h}:${m}:${s}`)
