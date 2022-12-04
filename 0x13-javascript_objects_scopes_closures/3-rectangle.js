#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w && w > 0 && h && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let pX = 'X';
    for (let y = 0; y < this.height; y++) {
      for (let x = 1; x < this.width; x++) {
        pX += 'X';
      }
      console.log(pX);
      pX = 'X';
    }
  }
};
