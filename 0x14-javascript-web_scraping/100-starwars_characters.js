#!/usr/bin/node
const request = require('request');
request.get('http://swapi.co/api/films/' + process.argv[2], function (err, res, body) {
  if (res.statusCode === 200) {
    for (const character of JSON.parse(body).characters) {
      request.get(character, function (err1, res1, body1) {
        if (res1.statusCode === 200) {
          console.log(JSON.parse(body1).name);
        } else if (err1) {
          console.log(err1);
        }
      });
    }
  } else if (err) {
    console.log(err);
  }
});
