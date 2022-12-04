#!/usr/bin/node
class Rectangle {
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

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
