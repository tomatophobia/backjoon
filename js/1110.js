const inputs = require('fs').readFileSync('input.txt').toString().trim().split(' ')

const original = inputs[0]
let result = ''
let lastDigit = ''
let firstDigit = ''
let cycle = 0
result = original.length === 2 ? original : original.padStart(2, '0');
while (true) {
  firstDigit = result[0]
  lastDigit = result[1]
  let sumResultLastDigit = (parseInt(firstDigit) + parseInt(lastDigit)) % 10
  result = lastDigit + sumResultLastDigit.toString()
  cycle++
  if (parseInt(result) === parseInt(original)) break
}

console.log(cycle)