const fs = require('fs');
const ts2110 = fs.readFileSync("input.txt").toString().trim().split("\n");
let a = ts2110[0].split(" ");
var c = a[1];
var len = a[0];
var lists = new Array();
for (var i = 1; i <= len; i++) {
  lists.push(ts2110[i]);
}
lists.sort(function (a, b) {
  return a - b;
});
var start = 1;
var end = lists[lists.length - 1] - lists[0];
var d = 0;
var anser = 0;
while (start <= end) {
  var mid = Math.floor((start + end) / 2);
  console.log(start, mid, end)
  var numst = lists[0];
  var cnt = 1
  for (var i = 1; i < len; i++) {
    d = lists[i] - numst;
    if (mid <= d) {
      cnt++;
      numst = lists[i];
    }
  }
  if (cnt >= c) {
    anser = start;
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}
console.log(anser);