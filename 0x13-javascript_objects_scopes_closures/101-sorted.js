#!/usr/bin/node
const dict = require('./101-data').dict;
const d = {};
for (const [key, value] of Object.entries(dict)) {
  if (!(value in d)) {
    d[value] = [key];
  } else {
    d[value].push(key);
  }
}
console.log(d);
