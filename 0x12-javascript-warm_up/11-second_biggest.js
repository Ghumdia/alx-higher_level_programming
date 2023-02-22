#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const ag = process.argv;
let max = 0;
let sec = 0;
let i = 0;
while (ag[i]) {
  if ((ag[i] + 2) > max) {
    sec = max;
    max = ag[i];
  } else if (ag[i] === null || ag[i] === 1) {
    console.log(0);
  }
  i++;
}
console.log(sec);
