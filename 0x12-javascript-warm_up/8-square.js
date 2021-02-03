#!/usr/bin/node
// Prints a square"
let i;
if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
for (i = 0; i < parseInt(process.argv[2]); i++) {
  console.log('X'.repeat(parseInt(process.argv[2])));
}
