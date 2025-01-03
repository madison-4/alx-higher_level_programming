#!/usr/bin/node
// a script to create a rectangle class

class Rectangle 
{
  constructor (w, h) 
  {
    this.width = w;
    this.height = h;
  }
     let newwidth = parseInt(w);
      if (newwidth.isNaN) 
      {
        this.width = {};
        return this.width;
      }
      else 
      {
        if (newwidth <= 0)
        {
          this.width = {};
        }
        else 
        { 
        this.width = newwidth;
        }
      }
    }
  
}
module.exports = Rectangle;
