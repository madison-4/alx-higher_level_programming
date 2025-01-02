#!/usr/bin/node
// a script to create a rectangle class

const Squares = require('./5-square.js');
class Square extends Squares {
    constructor (size) {
  super(size);
   }
  charPrint(c) {
  if (c === undefined) {
       c = 'X';
  }
   for (let i = 0; i < this.size; i++) {
     console.log(c.repeat(this.size));
	}
    }
}
module.exports = Square;
