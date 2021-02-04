#!/usr/bin/node
// Searches the second biggest integer in the list of arguments
const argument = process.argv;
let array;
if (isNaN(process.argv[2]) || process.argv.length === 3) {
  console.log(0);
} else {
  array = argument.slice(2);
  array.sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}
