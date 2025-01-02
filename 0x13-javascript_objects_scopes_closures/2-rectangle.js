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
}
module.exports = Rectangle;
