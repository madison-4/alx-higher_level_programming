#!/usr/bin/node
// a script to create a rectangle class
/**
 * it uses getters and setters
 */

class Rectangle {
  constructor (w, h) {
    if ((!(isNaN(w))) && (!(isNaN(h)))) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }
}
module.exports = Rectangle;
