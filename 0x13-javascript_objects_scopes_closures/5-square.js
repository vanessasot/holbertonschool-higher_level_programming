#!/usr/bin/node
// Create a Square class and inheritance with Rectangle
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
