#!/usr/bin/node
const request = require('request');

// process.argv[2] = url
// let's have fun with a ternary expression
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
