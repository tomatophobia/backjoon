const fs = require('fs');
const ts2110 = fs.readFileSync("input.txt").toString().trim().split("\n");
let a = ts2110[0].split(" ");
var c = parseInt(a[1], 10);
var len = parseInt(a[0], 10);
var lists = new Array();
for (var i = 1; i <= len; i++) {
  lists.push(parseInt(ts2110[i], 10));
}
lists.sort(function (a, b) {
  return a - b;
});

var start = 1;
var end = lists[lists.length - 1] - lists[0];

while (start < end) {
  var mid = Math.floor((start + end + 1) / 2);
  var numst = lists[0];
  var cnt = 1;
  for (var i = 1; i < len; i++) {
    var d = lists[i] - numst;
    if (mid <= d) {
      cnt++;
      numst = lists[i];
    }
  }

  if (cnt >= c) {
    start = mid;
  } else {
    end = mid - 1;
  }
}

console.log(end);