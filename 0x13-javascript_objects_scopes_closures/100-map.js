#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);
const newArr = list.map((mult, index) => mult * index);
console.log(newArr);
