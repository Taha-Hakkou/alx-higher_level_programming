#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
