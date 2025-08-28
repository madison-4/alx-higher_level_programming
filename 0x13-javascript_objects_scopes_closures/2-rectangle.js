#!/usr/bin/node
// a script to create a rectangle class

class Rectangle
{
  constructor (w, h)
  {
    this.width = w;
    this.height = h;
  }
    set width {
	let newwidth = parseInt(w);
	if (isNaN(newwidth)) {
	    this.width = {};
	}
	else if (newwidth <= 0) {
	    this.width = {};
	}
	else
	{
	    this.width = newwidth;
	}
    }
    set height {
	let newheight = parseInt(h);
	if (isNaN(newheight)) {
	    this.height = {};
	}
	else if (newheight <= 0) {
	    this.height = {};
	}
	else {
	    this.height = newheight;
	}
    }
}
module.exports = Rectangle;
