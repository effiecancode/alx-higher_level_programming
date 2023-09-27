#!/usr/bin/node
const request = require('request');

// process.argv[2] = movie Id
const baseUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(baseUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movietitle = JSON.parse(body);
    console.log(movietitle.title);
  }
});
