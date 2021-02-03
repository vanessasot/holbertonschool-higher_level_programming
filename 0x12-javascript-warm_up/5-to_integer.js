#!/usr/bin/node
// Prints two arguments passed to it.
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else if (!process.argv[2]) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2], 10));
}
