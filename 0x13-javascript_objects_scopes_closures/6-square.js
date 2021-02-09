#!/usr/bin/node
// Create a charPrint method
const square = require('./5-square');

module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let i;
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
