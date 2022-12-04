#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
}
let pX = 'X';
for (let y = 0; y < Number(process.argv[2]); y++) {
  for (let x = 1; x < Number(process.argv[2]); x++) {
    pX += 'X';
  }
  console.log(pX);
  pX = 'X';
}
