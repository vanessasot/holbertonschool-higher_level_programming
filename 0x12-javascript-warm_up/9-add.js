#!/usr/bin/node
// Prints the addition of 2 integers
function add (a, b) {
  const solution = a + b;
  return solution;
}
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
