#!/usr/bin/node
// a script to create a rectangle class
/**
 * a class that defines the width and height
 * It employs getters and setters
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const place = this.width;
    this.width = this.height;
    this.height = place;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
class Square extends Square {
  constructor(size) {
    super(size);
  }
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }

}
module.exports = Square;
