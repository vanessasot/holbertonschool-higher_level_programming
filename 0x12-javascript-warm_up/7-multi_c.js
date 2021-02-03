#!/usr/bin/node
// Prints x time "C is fun"
let i = 0;
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}
while (i < parseInt(process.argv[2])) {
  console.log('C is fun');
  i += 1;
}
